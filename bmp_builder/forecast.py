from fmi import FMI
from bmp_builder.handler import BMPHandler
from pathlib import PurePath
import os

from pytz import timezone
import datetime


class ForecastBitmap():
    def __init__(self, width, height, bmp_path, api_key, timezone_string, location):
        self.image_width = width
        self.image_height = height
        self.image = BMPHandler(self.image_width, self.image_height)
        self.save_path = PurePath(bmp_path)
        self.api_key = api_key
        self.timezone = timezone_string
        self.location = location
        self.fmi = FMI(self.api_key, place=self.location)

        self.symbol_folder = PurePath(os.path.dirname(__file__) + '/symbols')

        self.hours = 6
        self.step = 2

        self.v_margin = 5
        self.row_margin = 0

        self.left_row = int(self.image_width * (1/6))
        self.center_row = int(self.image_width * (3/6))
        self.right_row = int(self.image_width * (5/6))

        self.bitmap_name = self.api_key

    def create_bitmap(self):
        y_pointer = self.v_margin
        header_height = self._add_header(y_pointer)
        y_pointer += header_height + self.row_margin

        data = self.fmi.forecast()

        for i in range(0, self.hours * self.step, self.step):
            symbol_height = self._add_weather_row(data, y_pointer, i)
            y_pointer += symbol_height + self.row_margin

        self.image.save_to_path(self.save_path, self.bitmap_name)

    def _add_header(self, y_pointer):
        clock_symbol = self.symbol_folder.joinpath('clock.bmp')
        clock_width, clock_height = self.image.get_subimage_size(clock_symbol)
        x_left = self.left_row - int(clock_width / 2)
        self.image.add_subimage(clock_symbol, x_left, y_pointer)

        temp_symbol = self.symbol_folder.joinpath('temp.bmp')
        temp_width, temp_height = self.image.get_subimage_size(temp_symbol)
        x_center = self.center_row - int(temp_width / 2)
        self.image.add_subimage(temp_symbol, x_center, y_pointer)

        weather_symbol = self.symbol_folder.joinpath('weather_symbol.bmp')
        weather_width, weather_height = self.image.get_subimage_size(weather_symbol)
        x_right = self.right_row - int(weather_width / 2)
        self.image.add_subimage(weather_symbol, x_right, y_pointer)

        header_height = max(clock_height, temp_height, weather_height)
        return header_height

    def _add_weather_row(self, data, y_pointer, i):
        symbol = self.symbol_folder / '{0}.bmp'.format(data[i].weather_symbol)
        symbol_width, symbol_height = self.image.get_subimage_size(symbol)
        x_right = self.right_row - int(symbol_width / 2)
        self.image.add_subimage(symbol, x_right, y_pointer)

        time = data[i].time.astimezone(timezone(self.timezone))
        time_string = '{:%H}'.format(time)
        time_width, time_height = self.image.get_text_size(time_string)
        y_offset = int((symbol_height - time_height) / 2)
        x_left = self.left_row - int(time_width / 2)
        self.image.add_text(time_string, x_left, y_pointer + y_offset)

        temp_string = '{: ^5.0f}'.format(data[i].temperature)
        temp_width, temp_height = self.image.get_text_size(temp_string)
        temp_x = self.center_row - int(temp_width / 2)
        self.image.add_text(temp_string, temp_x, y_pointer + y_offset)

        return symbol_height

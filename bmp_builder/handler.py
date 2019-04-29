from PIL import Image, ImageDraw, ImageFont
from pathlib import PurePath
import os

class BMPHandler():
    def __init__(self, width_px, height_px):
        self.image_handler = Image.new('L', (width_px, height_px), color='white')
        self.image = ImageDraw.Draw(self.image_handler)
        font_path = str(PurePath(os.path.dirname(__file__) + '/fonts', 'FreeSansBold.ttf'))
        print(font_path)
        self.font = ImageFont.truetype(font_path, 20)

    def add_subimage(self, path_to_bmp, x, y):
        subimage = Image.open(str(path_to_bmp), 'r')
        self.image_handler.paste(subimage, (x, y))

    def get_subimage_size(self, path_to_bmp):
        return Image.open(str(path_to_bmp), 'r').size

    def add_text(self, text_string, x, y):
        self.image.text((x, y), text_string, font=self.font)

    def get_text_size(self, text_string):
        return self.image.textsize(text_string, font=self.font)

    def save_to_path(self, path, name):
        path = str(path.joinpath(name + '.bmp'))
        self.image_handler.save(path)

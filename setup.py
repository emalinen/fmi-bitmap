#!/usr/bin/env python
from distutils.core import setup

setup(
    name='BMP builder',
    version='0.0.7',
    description='BMP builder generates black and white bitmaps for e-paper displays',
    author='Esa Malinen',
    author_email='esa.malinen2@gmail.com',
    url='https://github.com/emalinen/fmi-bitmap',
    packages=['bmp_builder', 'bmp_builder.symbols', 'bmp_builder.fonts'],
    package_data={
        'bmp_builder': [
            'symbols/*.svg',
            'symbols/*.bmp',
            'fonts/*.ttf',
        ],
    },
    install_requires=[
        'pathlib',
        'pillow',
        'pytz',
        'fmi_weather',
    ],
)

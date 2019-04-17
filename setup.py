#!/usr/bin/env python
from distutils.core import setup

setup(
    name='BMP builder',
    version='0.0.2',
    description='BMP builder can build weather from FMI data',
    author='Esa Malinen',
    author_email='esa.malinen2@gmail.com',
    url='https://bitbucket.org/emalinen/python-fmi-image-builder/',
    packages=['bmp_builder', 'bmp_builder.symbols'],
    package_data={
        'bmp_builder': [
            'symbols/*.svg',
            'symbols/*.bmp',
        ],
    },
    install_requires=[
        'pathlib',
        'pillow',
        'pytz',
        'fmi',
    ],
    dependency_links=[
        'git+https://github.com/kipe/fmi.git#egg=fmi-0.50.1',
    ],
)

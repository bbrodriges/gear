import os

from setuptools import setup, find_packages

setup(
    name='gear',
    version='4.0.0',
    packages=find_packages(os.path.dirname(os.path.abspath(__file__))),
    install_requires=[
        'pbr',
    ],
)

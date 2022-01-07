import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "an_example_pypi_project",
    version = "0.0.1",
    author = "Jozef Tkocz",
    author_email = "jozeftkocz@gmail.com",
    description = ("Python wrapper for the weather API provided by https://www.weatherapi.com/"),
    packages=['an_example_pypi_project', 'tests'],
    long_description=read('README')
)
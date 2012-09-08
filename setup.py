import sys

from distutils.core import setup
from setuptools import find_packages

setup(
    name = 'runrunfootball',
    packages = find_packages(),
    tests_require = ['nose'],
    test_suite = 'nose.collector',
)

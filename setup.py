#!/usr/bin/env python

from setuptools import setup, find_packages
from pysparktools import __version__, __project__
from datetime import datetime

# create datetime based subversion
now = datetime.now()
today_date = datetime.strftime(now, '%Y%m%d')
today_time = datetime.strftime(now, '%H%M')
version_sub = '.' + today_date + '.' + today_time

setup(
    name = __project__,
    version = __version__ + version_sub,
    packages = find_packages(),
    description='Python pckage to simplify working with pyspark by using familiar pandas syntax.',
    python_requires='>=3.8.0, <3.10',
    install_requires=[]
)
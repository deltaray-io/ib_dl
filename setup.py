#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup

from setuptools import find_packages

install_reqs = [e.strip() for e in open("requirements.txt").readlines()]

setup(
    name='ib_dl',
    version='1.0',
    packages=find_packages(),
    url='https://github.com/tibkiss/ib_dl',
    license='Apache 2.0',
    author='Tibor Kiss',
    author_email='tibor.kiss@gmail.com',
    description='Historical market data downloader using Interactive Brokers TWS',
    install_requires=install_reqs,
    python_requires='>=3.6',
    entry_points={
       'console_scripts': [
           'ib-dl=ib_dl.download:main',
       ]
    }
)

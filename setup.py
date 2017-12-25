#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from distutils.core import setup

from setuptools import find_packages

import versioneer

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    if os.path.exists('README.md'):
        long_description = open('README.md').read()
    else:
        long_description=''

install_reqs = [e.strip() for e in open("requirements.txt").readlines()]

setup(
    name='ib_dl',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author='Tibor Kiss',
    author_email='tibor.kiss@gmail.com',
    description='Historical market data downloader using Interactive Brokers TWS',
    long_description=long_description,
    classifiers=[
             'Development Status :: 4 - Beta',
             'License :: OSI Approved :: Apache Software License',
             'Programming Language :: Python :: 3.6',
             'Topic :: Office/Business :: Financial :: Investment'],
    packages=find_packages(),
    url='https://github.com/tibkiss/ib_dl',
    license='Apache License, Version 2.0',
    install_requires=install_reqs,
    python_requires='>=3.6',
    entry_points={
       'console_scripts': [
           'ib-dl=ib_dl.download:main',
       ]
    }
)

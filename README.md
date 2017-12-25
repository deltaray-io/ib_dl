[![PyPI version](https://badge.fury.io/py/ib_dl.svg)](https://badge.fury.io/py/ib_dl)
[![Build Status](https://api.travis-ci.org/tibkiss/ib_dl.svg?branch=master)](https://travis-ci.org/tibkiss/ib_dl)
[![Docker Build Status](https://img.shields.io/docker/build/tibkiss/ib_dl.svg)](https://hub.docker.com/r/tibkiss/ib_dl/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

# Historical market data downloader 
Utility to download historical market data from Interactive Brokers.
The heavy lifting is done by [ib_insync](https://github.com/erdewit/ib_insync) project.

## Requirements
 * Python 3.6
 * [ib_insync](https://github.com/erdewit/ib_insync)
 * [IB's TWS API](http://interactivebrokers.github.io)
 
## Usage
 * Download and install IB TWS API
 * Install ib-dl with pip: `pip install ib_dl`
 * Start TWS, enable API access
 * Download data: `ib-dl SPY --duration "1 M" --bar-size "1 min" --tws-uri localhost:7492:999`

For further details see the help screen: `ib-dl --help`

## Docker
Docker images are provided under [tibkiss/ib_dl](https://hub.docker.com/r/tibkiss/ib_dl/)


## License
[Apache License Version 2.0](http://www.apache.org/licenses/)
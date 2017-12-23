# Historical market data downloader 
Utility to download historical market data from Interactive Brokers.
The heavy lifting is done by [ib_insync](https://github.com/erdewit/ib_insync) project.

## Requirements
 * Python 3.6
 * [ib_insync](https://github.com/erdewit/ib_insync)
 * [IB's TWS API](http://interactivebrokers.github.io)
 
## Usage
 * Install with pip: `pip install ib_dl`
 * Start TWS, enable API access
 * Download data: `ib_dl SPY "1 M" /path/to/dest/dir localhost:7492:999`

For further details see the help screen.

## License
[Apache License Version 2.0](http://www.apache.org/licenses/)
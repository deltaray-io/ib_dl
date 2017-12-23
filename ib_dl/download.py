import datetime
import logging

import click
from ib_insync import IB, Stock, util

logger = logging.getLogger(__name__)

LOCAL_TZ = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo


def download(symbol, period, dest_dir, host, port, client_id):
    logger.info("Downloading historical data of {symbol} for {period}".format(
        symbol=symbol, period=period))
    ib = IB()
    ib.connect(host, port, client_id)

    contract = Stock(symbol, exchange='SMART', currency='USD')
    bars = ib.reqHistoricalData(
        contract, endDateTime='', durationStr=period,
        barSizeSetting='1 min', whatToShow='TRADES', useRTH=True)

    df = util.df(bars)
    df.set_index('date', inplace=True)
    df.index = df.index.tz_localize(LOCAL_TZ).tz_convert('UTC')

    df.drop(columns=['average', 'barCount'], inplace=True)

    df.to_csv('%s/HC-%s-1M-ib.csv' % (dest_dir, symbol))


@click.command()
@click.argument('symbol')
@click.argument('period')
@click.argument('dest-dir')
@click.argument('uri', )
def main(symbol, period, dest_dir, uri):
    host = uri.split(':')[0]
    port = int(uri.split(':')[1])
    client_id = int(uri.split(':')[2])

    global logger
    logger = logging.getLogger()
    logging.basicConfig(level=logging.INFO)

    download(symbol, period, dest_dir, host, port, client_id)


if __name__ == '__main__':
    main()

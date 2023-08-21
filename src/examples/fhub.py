import aiohttp
import asyncio
import requests
import os
from datetime import datetime as dt, timedelta

dformat = '%Y-%m-%d'

def date(delta=None):

    d = dt.now()    
    if delta:
        d+=timedelta(days=delta)

    return d.strftime(dformat)

async def _get(endpoint):

    headers = {'X-Finnhub-Token': os.getenv('FINNHUB_KEY')}
    base_url = 'https://finnhub.io/api/v1/'

    async with aiohttp.ClientSession() as session:
        async with session.get(base_url + endpoint, headers=headers) as resp:
            return await resp.json()

async def get_symbols():
    return await _get('stock/symbol?exchange=US')

async def get_earnings_calendar(start=date(delta=-30), end=date(), symbol=None):

    url_str = f'/calendar/earnings?from={start}&to={end}'
    if symbol:
        url_str += f'&symbol={symbol}'

    return await _get(url_str)

async def get_social_sentiment(symbol):
    # hourly sentiment scores
    return await _get(f'/stock/social-sentiment?symbol={symbol}')

async def get_ohlcv(symbol, resolution='D', start=None, end=None):

    # returns close, high, low, open, status, timestamp, volume

    if start is None:
        start = int(dt.timestamp(dt.now() - timedelta(days=30))*1000)
    
    if end is None:
        end = int(dt.timestamp(dt.now())*1000)

    url_str = f'/stock/candle?symbol={symbol}&resolution={resolution}&' + \
        f'from={start}&to={end}'
    
    return await _get(url_str)

async def main():

    if False:
        syms = await get_symbols()
        print(syms)

    if False:
        test = await get_social_sentiment('AAPL')
        [print(t) for t in test['reddit']]
        
    if False:
        test = await get_earnings_calendar()
        [print(t) for t in test['earningsCalendar']]
    
    if True:
        test = await get_ohlcv('AAPL')
        [print(t) for t in test]
            
asyncio.run(main())
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from datetime import datetime as dt, timedelta
from data import Broker

b = Broker()

async def homepage(request):
    print(dir(request))
    print(request.query_params['test'])
    print(request.items())
    return JSONResponse({'homepage':'default index'})

async def get_instrument(request):
    symbol = request.query_params['symbol']
    return JSONResponse(b.instruments(symbol))

async def get_historical_quotes(request):
    symbol = request.query_params['symbol']
    return JSONResponse(b.get_historical_quotes(stock=symbol, interval='day', span='year'))

async def get_options(request):

    n = dt.now()
    
    # a bump up if already Friday
    if n.weekday() == 4:
        n+=timedelta(days=1)

    while n.weekday() != 4:
        n+=timedelta(days=1)
    d = dt.strftime(n, '%Y-%m-%d')

    symbol = request.query_params['symbol']
    return JSONResponse({
        "puts": b.get_options(stock=symbol, expiration_dates=[d], option_type='put'),
        "calls": b.get_options(stock=symbol, expiration_dates=[d], option_type='call')
    })

async def get_option_data(request):
    uuid = request.query_params['id']
    return JSONResponse(b.get_option_market_data(uuid)) 

async def get_news(request):
    symbol = request.query_params['symbol']
    return JSONResponse(b.get_news(symbol))

async def get_quotes(request):
    symbol = request.query_params['symbol']
    return JSONResponse(b.get_quotes(symbol))

async def get_spread(request):
    symbol = request.query_params['symbol']
    spread = b.get_spread(symbol)
    return JSONResponse({
        'ask': spread[0],
        'bid': spread[1]
    })

async def get_last(request):
    symbol = request.query_params['symbol']
    return JSONResponse(b.get_last(symbol))

middleware = [
    Middleware(CORSMiddleware, allow_origins=['*'])
]

app = Starlette(debug=True, routes=[
    Route('/instrument', get_instrument),
    Route('/historicals', get_historical_quotes),
    Route('/options', get_options),
    Route('/option', get_option_data),
    Route('/price', get_spread),
    Route('/news', get_news),
    Route('/quotes', get_quotes),
    Route('/last', get_last),
    Mount('/', app=StaticFiles(directory='static/dist'), name='static')
],
middleware=middleware)
from Robinhood import Robinhood
import os

"""
Flow:
    - get all instruments of interest -> enter in db
    
"""

class Broker():

    def __init__(self):

        self.rh = Robinhood()
        self.logged_in = self.rh.login(
            username=os.getenv('ROBIN_USER'), 
            password=os.getenv('ROBIN_PASS'),
            qr_code=os.getenv('ROBIN_QR')
        )

    def instruments(self, *args, **kwargs):
        return self.rh.instruments(*args, **kwargs)

    def get_historical_quotes(self, *args, **kwargs):
        return self.rh.get_historical_quotes(**kwargs)

    def get_options(self, *args, **kwargs):
        return self.rh.get_options(**kwargs)
    
    def get_option_market_data(self, *args, **kwargs):
        return self.rh.get_option_market_data(*args, **kwargs)

    def get_quotes(self, *args, **kwargs):
        return self.rh.quotes_data(*args, **kwargs)

    def get_news(self, *args, **kwargs):
        return self.rh.get_news(*args, **kwargs)

    def get_spread(self, *args, **kwargs):
        a = self.rh.ask_price(*args, **kwargs)
        b = self.rh.bid_price(*args, **kwargs)
        return (a[0][0], b[0][0])
    
    def get_last(self, *args, **kwargs):
        return self.rh.last_trade_price(*args, **kwargs)[0][0]

if __name__=="__main__":

    focus = ['MSFT', 'AAPL']
    b = Broker()
    print(f"LOGGED IN: {b.logged_in}")

    # instrument data
    # stock = b.instruments("MSFT")[0]
    # [print(f"{s}: {stock[s]}") for s in stock]

    # stock = b.get_quotes(focus)
    # print(stock)

    # q = b.get_quote_list('MSFT', 'ask_size')
    # print(q)

    # quote = b.get_historical_quotes(
        # stock="MSFT", interval='day', span='year')
    # [print(q) for q in quote['results'][0]['historicals']]
    
    # ps = rh.portfolios()
    # [print(f"{p}: {ps[p]}") for p in ps]

    # oh = rh.order_history()
    # [print(o) for o in oh['results']]

    # options
    # puts = rh.get_options('MSFT', expiration_dates=['2023-07-28'], option_type='put')
    # [print(p) for p in puts]

  


    #? OPTIONS

    # calls = rh.get_options('MSFT', expiration_dates=['2023-07-28'], option_type='call')
    # [print(c) for c in calls]
    
    # opts = b.get_option_market_data('f90656ae-8e57-4ec9-a2ba-d49122d529ec')
    # [print(f"{o}: {opts[o]}") for o in opts]
    # print(opts)
import requests as req
import datetime
import pandas as pd
from functools import cache
import os



class cc(object):

    
    def __init__(self, testing = False) -> None:
        if testing:
            print("Testing mode cc api...")
        

    @cache
    def btc_get_histo_daily(self):

        if os.path.isfile("cache/btc_histo.csv") and (datetime.datetime.today() - datetime.datetime.fromtimestamp(os.path.getmtime("cache/btc_histo.csv"))).days == 0:

            print("Using cache BTC price from today.")
            df = pd.read_csv("cache/btc_histo.csv")
            
            df['timestamp'] = [datetime.datetime.fromtimestamp(d) for d in df.time]

        else:

            data = req.get("https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&allData=true").json()['Data']['Data']
            df = pd.DataFrame(data)

            """N = 1000
            df = df.iloc[N: , :]
            df = df.reset_index(drop=True)"""

            df['timestamp'] = [datetime.datetime.fromtimestamp(d) for d in df.time]
            df.to_csv('cache/btc_histo.csv')

        return df
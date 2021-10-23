import json
import requests as req
import datetime
import pandas as pd
from functools import cache


class cc(object):

    
    def __init__(self, testing = False) -> None:
        if testing:
            print("Testing mode cc api...")
        

    @cache
    def btc_get_histo_daily(self):
        data = req.get("https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&allData=true").json()['Data']['Data']
        df = pd.DataFrame(data)
        df['timestamp'] = [datetime.datetime.fromtimestamp(d) for d in df.time]
        return df
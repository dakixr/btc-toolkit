import json
import requests as req
import datetime
import pandas as pd


class cc(object):

    api_key = None
    
    def __init__(self, api_key, testing = False) -> None:
        self.api_key = api_key
    
    def get_all_btc_daily(self):
        data = req.get("https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&allData=true").json()['Data']['Data']
        df = pd.DataFrame(data)
        df['timestamp'] = [datetime.datetime.fromtimestamp(d) for d in df.time]
        df['i'] = [ i for i in range(len(df))]
        return df
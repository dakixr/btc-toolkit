import json
import requests as req

class cmc(object):

    api_key = None
    
    def __init__(self, api_key, testing = False) -> None:
        self.api_key = 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c' if testing else api_key
        self.base_url = 'https://sandbox-api.coinmarketcap.com/v1' if testing else 'https://pro-api.coinmarketcap.com/v1'

        if testing:
            print("TESTING MODE ENABLED: The data will not be usable to real investing, use only for developing/testing.")

    def listing_rank(self, start = 1, limit = 50, fiat = 'USD'):

        url = self.base_url + '/cryptocurrency/listings/latest'

        parameters = {
            'start': start,
            'limit': limit,
            'convert': fiat
            } 

        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': self.api_key,
            }
            
        response = req.get(url = url, params = parameters, headers = headers)
        return dict(json.loads(response.text))


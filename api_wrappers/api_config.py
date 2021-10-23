def init(api_keys):
    '''Initialize API's...'''
    global cmc_key, crypto_compare_key

    # Make visible api keys
    cmc_key = api_keys["cmc"]
    crypto_compare_key = api_keys["cryptocompare"]
    

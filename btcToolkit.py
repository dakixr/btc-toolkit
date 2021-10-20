import argparse

def main():

    # Arguments
    parser = argparse.ArgumentParser(description = 'This is a BTC toolkit')
    parser.add_argument('-k', '--API_KEY_CoinMarketCap', action="store", required=True)
    parser.add_argument('-t', '--testing', action='store_true', default=False, help='Activate testing mode')
    args = parser.parse_args()

    # API CMC
    import cmc_api
    cmc = cmc_api.cmc(args.API_KEY_CoinMarketCap, testing = args.testing)
    print(cmc.listing_rank(limit=1))

if __name__ == "__main__":
    main()
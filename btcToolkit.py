import argparse
import yaml
from yaml.loader import SafeLoader
from api_wrappers import crypto_compare_api as cc_api
import btc_views


def main():

    # Arguments
    parser = argparse.ArgumentParser(description = 'This is a BTC toolkit')
    parser.add_argument('-k', '--api_keys_file', action="store", default="api_keys.yaml")
    parser.add_argument('-t', '--testing', action='store_true', default=False, help='Activate testing mode')
    args = parser.parse_args()

    # Read API keys
    api_keys = yaml.load(open(args.api_keys_file), Loader=SafeLoader)

    # Create crypto compare client
    cc = cc_api.cc(api_keys["cryptocompare"])


    # Testing to represent all BTC data in log scale
    df = cc.get_all_btc_daily()
    btc_views.log_fitted(df)

    

if __name__ == "__main__":
    main()
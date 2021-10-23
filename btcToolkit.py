import argparse
import yaml
from yaml.loader import SafeLoader


def main():

    # Arguments
    parser = argparse.ArgumentParser(description = 'This is a BTC toolkit')
    parser.add_argument('-k', '--api_keys_file', action="store", default="api_keys.yaml")
    parser.add_argument('-t', '--testing', action='store_true', default=False, help='Activate testing mode')
    args = parser.parse_args()

    # Read and init API keys
    api_keys = yaml.load(open(args.api_keys_file), Loader=SafeLoader)
    from api_wrappers import api_config
    api_config.init(api_keys)

    # Create btc controller
    from btc import btc_controler
    btc = btc_controler.btc_controller()

    ###################################################################################

    btc.log_fit()
    btc.log()
    btc.plot()



if __name__ == "__main__":
    main()
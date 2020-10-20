#! python3

from gather_data.gather import gather_main
from gcp.bq import test_query
from coinbase.pro_api import get_products, get_historic_rates

if __name__ == '__main__':
    # gather_main()
    test_query()
    # get_products('btc')
    # get_historic_rates('BTC-USD')

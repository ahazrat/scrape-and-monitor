import requests

# rest_api_endpoint_old = 'https://api-public.sandbox.pro.coinbase.com'  # 404
rest_api_endpoint_url = 'https://api.pro.coinbase.com'


def get_time():
    response = requests.get(rest_api_endpoint_url + '/time')
    print(f'Coinbase time: {response.json()}')


def get_currencies():
    response = requests.get(rest_api_endpoint_url + '/currencies')
    print('Available Currencies:')
    for currency in response.json():
        print(f"{currency['id']} ({currency['name']}): {currency['status']}")


def get_products(product_filter=None):
    response = requests.get(rest_api_endpoint_url + '/products')
    for product in response.json():
        if product_filter is not None:
            if product_filter in str(product['id']).lower():
                print(product)
        else:
            print(product)


def get_product_ticker(product_id):
    response = requests.get(rest_api_endpoint_url + '/products/' + product_id + '/ticker')
    print(response.json())


def get_historic_rates(product_id: str):
    """
    Historic rates for a product.
    Rates are returned in grouped buckets based on requested granularity.
    Historical rate data may be incomplete.
    No data is published for intervals where there are no ticks.
    Historical rates should not be polled frequently.
    If you need real-time information, use the trade and book endpoints along with the websocket feed.

    RESPONSE ITEMS
    Each bucket is an array of the following information:
    - time: bucket start time
    - low: lowest price during the bucket interval
    - high: highest price during the bucket interval
    - open: opening price (first trade) in the bucket interval
    - close: closing price (last trade) in the bucket interval
    - volume: volume of trading activity during the bucket interval
    """
    response = requests.get(rest_api_endpoint_url + '/products/' + product_id + '/candles')
    historic_rates = response.json()
    print('historic_rates:')
    for candle in historic_rates:
        print(candle)
    return historic_rates


if __name__ == '__main__':
    print('loading coinbase data')
    get_time()
    # get_currencies()
    # get_products('bch')
    get_product_ticker('BCH-USD')

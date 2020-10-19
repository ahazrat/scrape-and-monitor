import requests


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


if __name__ == '__main__':
    print('loading coinbase data')
    # rest_api_endpoint_old = 'https://api-public.sandbox.pro.coinbase.com'  # 404
    rest_api_endpoint_url = 'https://api.pro.coinbase.com'
    get_time()
    # get_currencies()
    # get_products('bch')
    get_product_ticker('BCH-USD')

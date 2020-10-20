
from coinbase.pro_api import get_time


def gather_main():
    sources = ['coinbase']
    if 'coinbase' in sources:
        get_time()


from gather_data.coinbase_pro import get_time


def gather_main():
    sources = ['coinbase']
    if 'coinbase' in sources:
        get_time()

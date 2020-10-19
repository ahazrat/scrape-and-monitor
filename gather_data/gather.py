
from gather_data.coinbase_pro import ping_coinbase


def gather_main():
    sources = ['coinbase']
    if 'coinbase' in sources:
        ping_coinbase()

#!/usr/bin/env python

import sys, time
from requests import request
from json import loads

# prices api
CRYPTO_API = 'https://api.coinmarketcap.com/v1/ticker/'
STANDARD_API = 'https://www.google.com/finance/info?q='

# crypto symbols
CRYPTO_SYMBOLS = {'btc':'bitcoin', 'ltc':'litecoin', 'eth':'ethereum'}

def getCrypto(symbol):
    """Pull data for cryptocurrencies
    """

    try:
        price = request('get', '{}{}/'.format(CRYPTO_API, CRYPTO_SYMBOLS[symbol]))
        json_price = loads(price.text)

    except:
        sys.exit(0)

    price = json_price[0]['price_usd']
    current_time = time.strftime('%Y/%m/%d %X')

    return '{} {} ${}'.format(current_time, symbol, price)

def getStandard(symbol):
    """Pull data for standard symbols
    """

    try:
        price = request('get', '{}{}'.format(STANDARD_API, symbol))
        json_price = loads(price.text.replace('// ', ''))

    except:
        sys.exit(0)

    price = json_price[0]['l']
    current_time = time.strftime('%Y/%m/%d %X')

    return '{} {} ${}'.format(current_time, symbol, price)

if __name__ == '__main__':
    
    # check if symbol is a cryptocurrency
    if sys.argv[1].lower() in CRYPTO_SYMBOLS:
        print(getCrypto(sys.argv[1].lower()))

    # everything else, send to the standard api
    else:
        print(getStandard(sys.argv[1]))

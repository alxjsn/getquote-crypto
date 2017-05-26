getquote-crypto
===============
I needed a way to update my prices for cryptocurrencies automatically with ledger-cli while still being able to update standard prices. Here we go.

getquote.py
-----------
A script to be used in combination with the `--download` or `-Q` argument for ledger-cli.

### Installation
1. pip install requests
2. sudo cp getquote.py /usr/local/bin/getquote
3. touch ~/.pricedb
4. echo '--price-db ~/.pricedb\n--download' >> ~/.pricedb

Now when ledger-cli is run with an argument such as `--market` or `-V` the pricedb will be updated with the latest prices for any symbols used in the ledger file.

### API Settings
- Cryptocurrency (Bitcoin/btc, Litecoin/ltc, and Ethereum/eth) prices are retreived from `https://api.coinmarketcap.com/v1/ticker/[symbol]`.
- Standard prices are retrieved from `https://www.google.com/finance/info?q=[symbol]`

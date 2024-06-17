# api = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'


import requests

URL = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
res = requests.get(URL)
print(res.content)
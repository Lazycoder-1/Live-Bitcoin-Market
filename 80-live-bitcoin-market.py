# api = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
import time
import datetime
import requests


API_KEY = '97655b6a-ee07-4105-82a4-b82976527a2b'
URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

# Define headers including the API key
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_KEY,
}

res = requests.get(URL, headers=headers)
data = res.json()

# Extract Bitcoin data and update the value of bitcoin in every 5 seconds
while 1 == 1:
    API_KEY = '97655b6a-ee07-4105-82a4-b82976527a2b'
    URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    bt_time = datetime.datetime.now().strftime("%d, %b %Y %H:%M:%S")
    for cryptocurrency in data['data']:
        if cryptocurrency['symbol'] == 'BTC':
            bitcoin_price = cryptocurrency['quote']['USD']['price']
            print('{}: {}'.format(bt_time,bitcoin_price))
            time.sleep(5)
            break

# api = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'
import time
import requests

# Replace 'YOUR_API_KEY' with your actual API key from CoinMarketCap
API_KEY = '97655b6a-ee07-4105-82a4-b82976527a2b'
URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

# Define headers including the API key
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_KEY,
}

res = requests.get(URL, headers=headers)
data = res.json()

# Extract Bitcoin data
while 1 == 1:
    API_KEY = '97655b6a-ee07-4105-82a4-b82976527a2b'
    URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    for cryptocurrency in data['data']:
        if cryptocurrency['symbol'] == 'BTC':
            bitcoin_price = cryptocurrency['quote']['USD']['price']
            print(f"The current value of Bitcoin is: ${bitcoin_price:.2f}")
            time.sleep(5)
            break


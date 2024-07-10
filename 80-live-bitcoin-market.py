# api = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/'


import requests

# Replace 'YOUR_API_KEY' with your actual API key from CoinMarketCap
API_KEY = '97655b6a-ee07-4105-82a4-b82976527a2b'
URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

# Define headers including the API key
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': API_KEY,
}

# Make a request to the API
res = requests.get(URL, headers=headers)

# Convert the response to JSON
data = res.json()

# Print the data
print(data)







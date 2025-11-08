import requests, sys,json

api_key = '093acbcd4ec6048b775d7f662761c08852534d61b8b8ffa9e0b209d96328a945'

url = f'https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}'

r = requests.get(url)
data = r.json()

price_usd = float(data["data"]["priceUsd"])
supply = float(data["data"]["supply"])


print("coin  :", str(data["data"]["id"]))
print(f"price : ${price_usd}")
print(f"supply: {supply}")





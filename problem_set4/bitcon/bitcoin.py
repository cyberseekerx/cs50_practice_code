import requests,sys, json

api_key = "093acbcd4ec6048b775d7f662761c08852534d61b8b8ffa9e0b209d96328a945"
url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"
playload = {"data": "priceUsd"}
r = requests.get(url)
data = r.json()
try:
    if len(sys.argv) == 0: 
        sys.exit("Missing command-line argument")
    elif sys.argv[1].isalpha():
        sys.exit("Command-line argument is not a number")
except requests.RequestException:
        print("not this")

priceUsd = float((data["data"]["priceUsd"]))

if len(sys.argv) > 1 :
    amount = priceUsd * float(sys.argv[1])
    res = "{:,}".format(amount)
    print(f"${amount:,.4f}")
else:
    print("not working")

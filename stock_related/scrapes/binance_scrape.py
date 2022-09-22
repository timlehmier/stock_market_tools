# import our libraries
import requests
import json


def filter_by_price(currencies, price):
    for currency in currencies:
        # print(currency['askPrice'])
        if currency['askPrice'] > price:
            return currency;

r = requests.get('https://api2.binance.com/api/v3/ticker/24hr')
currencies = r.json();
# for currency in currencies:
#     print(filter_by_price(currency, ))
# parsed = json.loads(currencies);
# filtered_currencies = filter_by_price(currencies, '5')
print(json.dumps(currencies, indent=4, sort_keys=True))


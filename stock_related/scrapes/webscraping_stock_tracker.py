#import dependencies
import requests
from bs4 import BeautifulSoup
import json
import csv
import pandas as pd

mystocks = ['SPY', 'TSLA', 'QQQ', 'VIX']
stockdata = []

def getData(symbol):
  headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
  url = f'https://finance.yahoo.com/quote/{symbol}'  
  r = requests.get(url, headers=headers)
  soup = BeautifulSoup(r.text, 'html.parser')
  stock = {
    'symbol': symbol,
    'Price Tracker' : soup.find('div', {'class':'D(ib) Mend(20px)'}).text}
  return stock

for item in mystocks:
  stockdata.append(getData(item))
  print('Getting: ', item)
    
df = pd.DataFrame(stockdata)
print(df)

#df.to_csv('stockdata.csv', index=False, header=True, sep=':')

# Obtain every title of columns with tag <th>
#header = []
#for i in df.find():
 #title = i.text
 #header.append(title)
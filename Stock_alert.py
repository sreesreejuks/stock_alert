# Import required modules
from lxml import html
import requests
import pandas as pd
from share_data import dict


stock_name = input('Enter stock name: ')
stock_exchange_name = dict[stock_name]

url = 'https://www.google.com/finance/quote/' + stock_exchange_name
alert = float(input('Enter the alert: '))

# Request the page
page = requests.get(url)

# Parsing the page
tree = html.fromstring(page.content)

# Get element using XPath
prices = tree.xpath(
    '//div[@class="YMlKec fxKbKc"]/text()')
# print(prices)
price = prices[0]
price = float(price[3:])
# print('This vallue', price[3:])
# price= 405
if alert > price:
    print('price is below', alert, 'Current price is', price)

else:
    print('Price is above', alert, 'Current price is', price)

# df = pd.DataFrame([{'Price': price}])
# df.to_csv('sneakers.csv', index=False, encoding='utf-8')

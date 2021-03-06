# Import required modules
from lxml import html
import requests
# import pandas as pd
# from share_data import dict

# stock input & accessing dictionary
stock_name = input('Enter stock name: ')

"""for key in list(dict.keys()):
    if key == stock_name:
        stock_exchange_name = dict[stock_name]
    else:
        stock_exchange_name = stock_name
"""
# setting alert price
alert = float(input('Enter the alert: '))

# Checking given name in dictionary for actual name
# stock_exchange_name = dict[stock_name]
stock_exchange_name = stock_name

# calling the site.
# url = 'https://www.google.com/finance/quote/' + stock_exchange_name
url = 'https://www.google.com/finance/quote/' + stock_name

# Request the page
page = requests.get(url)

# Parsing the page
tree = html.fromstring(page.content)

# Get element using XPath
prices = tree.xpath(
    '//div[@class="YMlKec fxKbKc"]/text()')
#print(prices)

# by default there is rupee symbol in front of the price (ex: ₹238.20), below command is to remove the symbol
price = prices[0]
price = float(price[3:])


# Comparing the alert price and the actual price.
def compare_prices():
    if price < alert:
        print('The following price alert has been triggered.', '\nSymbol:', stock_exchange_name, '\nCurrent price:',
              price, '\nTrigger set:', 'less than', alert)
        # print('Stock price is below', alert, 'the current price is', price) # uncomment to test
    # below code is for saving the data to csv, only if the alert price is less than or equal to current price
    # df = pd.DataFrame([{'Stock name': stock_exchange_name, 'Current Price': price, 'Trigger set': alert}])
    # df.to_csv('report.csv', index=False, encoding='utf-8')
    elif price == alert:
        print('The following price alert has been triggered.', '\nSymbol:', stock_exchange_name, '\nCurrent price is',
              price, '\nTrigger set:', 'equal to', alert)
        # df = pd.DataFrame([{'Stock name': stock_exchange_name, 'Current Price': price, 'Trigger set': alert}])
        # df.to_csv('report.csv', index=False, encoding='utf-8')
    else:
        print('Stock Price is above', alert, 'the current price is', price)


compare_prices()

# df = pd.DataFrame([{'Price': price}])
# df.to_csv('sneakers.csv', index=False, encoding='utf-8')

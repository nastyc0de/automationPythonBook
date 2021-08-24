import re
import delorean
from decimal import Decimal

log = '[2018-05-05T11:07:12.267897] - SALE - PRODUCT: 1345 - PRICE: $09.99'
# slip the logs into its parts. we ignore the SALE (doesnt add any relevant information)
divide_it = log.split(' - ');
timestamp_string, _, product_string, price_string = divide_it

# parse the timestamp into datetime object:
timestamp = delorean.parse(timestamp_string.strip('[]'))

# parse the product id into an integer
product_id = int(product_string.split(':')[1])

# parse the price into a decimal
price = Decimal(price_string.split('$')[1])

#using POO 
class PriceLog:
    def __init__(self, timestamp, product_id, price):
        self.timestamp = timestamp
        self.product_id = product_id
        self.price = price
    def __repr__(self):
        return '<PriceLog ({}, {}, {})>'.format(self.timestamp, self.product_id, self.price)
    
    @classmethod
    def parse(cls, text_log):
        divide_it = text_log.split(' - ');
        timestamp_string, _, product_string, price_string = divide_it
        timestamp = delorean.parse(timestamp_string.strip('[]'))
        product_id = int(product_string.split(':')[1])
        price = Decimal(price_string.split('$')[1])
        return cls(timestamp= timestamp, product_id=product_id, price=price)

# using a 3rd party tool (Parse)
from parse import parse

# analyze it and describe it as you would do.
# format_info = '[{date}] - SALE - PRODUCT: {product} - PRICE: ${price}'
# result = parse(format_info, log)
# print(result)
# print(result['date'], result['product'], result['price'])

# all data are string. We can define the types to be parsed.
# format_info = '[{date:ti}] - SALE - PRODUCT: {product:d} - PRICE: ${price:05.2f}'
# result = parse(format_info, log)
# print(result)
# print(type(result['date']), type(result['product']), type(result['price']))

# define a custom type price.
def price(string):
    return Decimal(string)

format_info = '[{date:ti}] - SALE - PRODUCT: {product:d} - PRICE: ${price:price}'
result = parse(format_info, log, {'price': price})
print(result)
print(type(result['date']), type(result['product']), type(result['price']))

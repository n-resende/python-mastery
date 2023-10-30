# stock.py

import csv
from decimal import Decimal
from reader import read_csv_as_instances

class Stock:
    types = (str, int, Decimal)
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)
        
    def cost(self):
        return self.shares * self.price
    
    def sell(self, nshares):
        self.shares -= nshares
        
class Row:
    def __init__(self, route, date, daytype, numrides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.numrides = numrides
        
    @classmethod
    def from_row(cls, row):
        return cls(row[0], row[1], row[2], int(row[3]))
        
def print_portfolio(portfolio):
    print('%10s %10s %10s' % ('name', 'shares', 'price'))
    print("-" * 10, "-" * 10, "-" * 10)
    for s in portfolio:
        print('%10s %10d %10.2f' % (s.name, s.shares, s.price))

if __name__ == '__main__':
    portfolio = read_csv_as_instances('Data/portfolio.csv', Stock)    
    print_portfolio(portfolio)
    
    rides = read_csv_as_instances('Data/ctabus.csv', Row)
    print(len(rides))
    
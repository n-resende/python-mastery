# stock.py

import csv
from reader import read_csv_as_instances
from decimal import Decimal

class Stock:
    __slots__ = ['name', '_shares', '_price']
    
    _types = (str, int, Decimal)
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)
    
    @property
    def cost(self):
        return self.shares * self.price
    
    @property
    def shares(self):
        return self._shares
    
    @shares.setter
    def shares(self, value):
        if not isinstance(value, self._types[1]):
            raise TypeError(f"Expected {self._types[1].__name__}")
        if value < 0:
            raise ValueError('Expected positive number')
        self._shares = value
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if not isinstance(value, self._types[2]):
            raise TypeError(f"Expected {self._types[2].__name__}")
        if value < 0:
            raise ValueError('Expected positive number')
        self._price = value
            
    
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
    print(portfolio[0].cost)
    
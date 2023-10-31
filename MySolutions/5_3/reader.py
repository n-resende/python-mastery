# reader.py

import csv
from typing import Type, List, TextIO
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
        
    def __repr__(self):
        return f"Stock('{self.name}', {self.shares}, {self.price})"
        
    def __eq__(self, other):
        return isinstance(other, Stock) and ((self.name, self.shares, self.price) == (other.name, other.shares, other.price)) 

def csv_as_dicts(lines: TextIO, types: List, *, headers=None) -> List:
    return convert_csv(lines, lambda headers, row: { name: func(val) for name, func, val in zip(headers, types, row) })


def csv_as_instances(lines: TextIO, cls: Type, *, headers=None) -> List:
    return convert_csv(lines, lambda headers, row: cls.from_row(row))

def read_csv_as_dicts(filename: str, types: List, *, headers=None) -> List:
    '''
    Read CSV data into a list of dictionaries with optional type conversion
    '''
    with open(filename) as file:
        return csv_as_dicts(file, types, headers=headers)

def read_csv_as_instances(filename: str, cls: Type, *, headers=None) -> List:
    '''
    Read CSV data into a list of instances
    '''
    with open(filename) as file:
        return csv_as_instances(file, cls, headers=headers)

def convert_csv(lines: TextIO, func, *, headers=None) -> List:
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    return list(map(lambda row: func(headers,row), rows))
        
def make_dict(headers, row):
    return dict(zip(headers,row))

lines = open('Data/portfolio.csv')
result = convert_csv(lines, make_dict)
print(result)
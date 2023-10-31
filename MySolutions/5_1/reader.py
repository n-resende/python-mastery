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
    '''
    Read CSV data into a list of dictionaries with optional type conversion
    '''
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = { name: func(val) for name, func, val in zip(headers, types, row)}
        records.append(record)
    return records

def csv_as_instances(lines: TextIO, cls: Type, *, headers=None) -> List:
    '''
    Convert lines of CSV data into a list of instances
    '''
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records

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
        
port = read_csv_as_dicts('Data/portfolio.csv', [str, int, Decimal])
print(port)

port = read_csv_as_instances('Data/portfolio.csv', Stock)
print(port)
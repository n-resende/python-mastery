# stock.py

import csv

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
        
    def cost(self):
        return self.shares * self.price
    
    def sell(self, nshares):
        self.shares -= nshares

    
def read_portfolio(filename):
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        data = []
        for row in rows:
            name = row[0]
            shares = int(row[1])
            price = float(row[2])
            data.append(Stock(name, shares, price))
    
    return data
        
def print_portfolio(portfolio):
    print('%10s %10s %10s' % ('name', 'shares', 'price'))
    print("-" * 10, "-" * 10, "-" * 10)
    for s in portfolio:
        print('%10s %10d %10.2f' % (s.name, s.shares, s.price))

if __name__ == '__main__':
    s = Stock('ab', 100, 5)
    print(s.shares)
    s.sell(25)
    print(s.shares)

    portfolio = read_portfolio('Data/portfolio.csv')    
    print_portfolio(portfolio)
    
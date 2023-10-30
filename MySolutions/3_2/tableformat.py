import stock

def print_table(data, attributes):
    
    print(' '.join('%10s' % attr for attr in attributes))
    print(("-" * 10 + " ")*len(attributes))
    for s in data:
        print(' '.join('%10s' % getattr(s, attr) for attr in attributes))
        
if __name__ == '__main__':
    portfolio = stock.read_portfolio('Data/portfolio.csv')
    print_table(portfolio, ['name', 'shares', 'price'])

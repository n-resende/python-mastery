# pcost.py

def calculate_stock_prices():
    stocks = open('./Data/portfolio.dat', 'r').read().split()
    total_price = 0.0
    
    for i in range(int(len(stocks)/3)):
        number_of_shares = int(stocks[(i*3)+1])
        stock_price = float(stocks[(i*3)+2])
        total_price += number_of_shares * stock_price
    
    return total_price

if __name__ == '__main__':
    print(f'Total stock price: ${calculate_stock_prices()}')
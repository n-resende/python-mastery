# pcost.py

def portfolio_cost(filename):
    total_price = 0.0
    
    with open(filename, 'r') as f:
        for line in f:
            stock = line.split()
            try:
                number_of_shares = int(stock[1])
                stock_price = float(stock[2])
                total_price += number_of_shares * stock_price
            except Exception as e:
                print(f"Couldn't parse: {line}Reason: {e}\n")
                
    return total_price

if __name__ == '__main__':
    #1_4(a)
    print(f'Total stock price: ${portfolio_cost("../../Data/portfolio.dat")}')
    
    #1_4(b)
    print(f'Total stock price: ${portfolio_cost("../../Data/portfolio3.dat")}')
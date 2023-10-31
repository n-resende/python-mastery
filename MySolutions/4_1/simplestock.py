class SimpleStock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.shares * self.price
    
goog = SimpleStock('GOOG', 100, 42.0)
print(goog.__dict__)

goog.date = '6/11/2007'
print(goog.__dict__)

goog.__dict__['time'] = '9:45am'
print(goog.time)

print(goog.__class__)
print(goog.cost())
print(SimpleStock.__dict__['cost'])
print(SimpleStock.__dict__['cost'](goog))

SimpleStock.spam = 42
print(goog.spam)
print(goog.__dict__)
print(SimpleStock.__dict__['spam'])
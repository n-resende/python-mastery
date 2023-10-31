def typedproperty(expected_type):
    class TypedProperty:
        def __set_name__(self, owner, name):
            self.name = '_' + name

        def __get__(self, instance, owner):
            return getattr(instance, self.name)

        def __set__(self, instance, value):
            if not isinstance(value, expected_type):
                raise TypeError(f'Expected {expected_type}')
            setattr(instance, self.name, value)

    return TypedProperty()

String = lambda: typedproperty(str)
Integer = lambda: typedproperty(int)
Float = lambda: typedproperty(float)

class Stock:
    name = String()
    shares = Integer()
    price = Float()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
        
s = Stock('a', 10, 5.0)
print(s)
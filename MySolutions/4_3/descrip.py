class Descriptor:
    def __init__(self, name):
        self.name = name
    def __get__(self, instance, cls):
        print('%s:__get__' % self.name)
    def __set__(self, instance, value):
        print('%s:__set__ %s' % (self.name, value))
    def __delete__(self, instance):
        print('%s:__delete__' % self.name)
        
class Foo:
        a = Descriptor('a')
        b = Descriptor('b')
        c = Descriptor('c')
     
f = Foo()   
print(f) 
print(f.a)
print(f.b)
f.a = 23
print(f.a)
del f.a
print(f.a)
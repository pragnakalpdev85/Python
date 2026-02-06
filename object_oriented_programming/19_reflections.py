#type()
print (type(10))
print (type(2.55))
print (type("Hello World"))
print (type([1,2,3,5,6,7,8]))
print (type({1:'one', 2:'two'}))

#isinstance()
print(isinstance(10, int))
print(isinstance("Hello",str))

# issubclass()
print(issubclass(int, object))

# callable()
def test():
    pass

print(callable("Hello"))
print(callable(test))

# getattr()
class Person:
    def __init__(self, name):
        self.name = name
        
person = Person("John")
print(getattr(person, "name"))

# setattr()
class Person:
    def __init__(self, name):
        self.name = name
        
person = Person("John")
setattr(person, "name","Alice")
print(person.name)

#hasattr() 
class Person:
    def __init__(self, name):
        self.name = name
        
person = Person("John")
print(hasattr(person, "name"))

#dir()
class Person:
    def __init__(self, name):
        self.name = name

print(dir(Person))


#using init
class Singleton:
    __uniqueInstance = None
    
    @staticmethod
    def createInstance():
        if Singleton.__uniqueInstance == None:
            Singleton()
        return Singleton.__uniqueInstance
    
    def __init__(self):
        if Singleton.__uniqueInstance != None:
            print("Object Already exists")
        else:
            Singleton.__uniqueInstance = self
            
obj1 = Singleton.createInstance()
print(obj1)
obj2 = Singleton.createInstance()
print(obj2)

class Singleton:
    __uniqueInstance = None
    
    def __new__(cls):
        if Singleton.__uniqueInstance is None:
            cls.__uniqueInstance = super(Singleton, cls).__new__(cls)
            
        return cls.__uniqueInstance
    
obj1 = Singleton()
print(obj1)
obj2 = Singleton()
print(obj2)

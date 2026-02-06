from abc import ABC, abstractmethod

#abstraction
class demo(ABC):
    #abstarct method
    @abstractmethod
    def method1(self):
        print ("abstract method")
        return
    
    #normal implemented method
    def method2(self):
        print ("concrete method")
        
#interfaces
#formal interface using abc module
class demo(ABC):
    
    @abstractmethod
    def method1(self):
        print ("abstract method 1")
        return
    
    @abstractmethod
    def method2(self):
        print ("abstract method 2")

#informal interface      
class demo:
    
    def method1(self):
        pass
    
    def method2(self):
        pass
    
#implementation class 
class imple(demo):
    def method1(self):
        print("Implemented method 1")
        
    def method2(self):
        print("Implemented method 2")

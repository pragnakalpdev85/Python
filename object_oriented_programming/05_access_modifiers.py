class Employee:
    def __init__(self, name, age, salary):
        self.name = name #public member
        self._salary = salary #protected member
        self.__age = age #private member
        
    def display_employee(self):
        print(f"Name: {self.name}, Age: {self.__age}, Salary: {self._salary}")
        
emp1 = Employee("John",25,25000)
emp1.display_employee()

#name mangling
print(emp1._Employee__age)

#property method
class Employee:
    def __init__(self, name):
        self._name = name
    
    def getter(self):
        print("get value")
        return self._name
    
    def setter(self,name):
        print("set value",name)
        self._name = name
        
    def deleter(self):
        print("delete value")
        del self._name
        
    name = property(getter, setter, deleter)
    
emp2 = Employee("John")
print(emp2.name)
emp2.name = "Alice"
del emp2.name
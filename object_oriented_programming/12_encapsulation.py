#encapsulation
class Employee:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        
    def display(self):
        print(f"Name: {self.__name}, Age: {self.__age}")
        
emp = Employee("John",25)
emp.display()
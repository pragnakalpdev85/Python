#hybrid inheritance
class CEO:
    def display_CEO(self):
        print("CEO Class")
        
class Manager:
    def display_manager(self):
        print("Manager Class")
        
class Employee1(Manager):
    def display_employee1(self):
        print("Employee class 1")
        
class Employee2(CEO,Manager):
    def display_employee2(self):
        print("Employee class 2")
        
emp1 = Employee1()
emp1.display_employee1()
emp1.display_manager()

emp2 = Employee2()
emp2.display_employee2()
emp2.display_CEO()
emp2.display_manager()
        
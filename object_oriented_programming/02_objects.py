#creating class
class Employee:
    #class attribute
    employee_count = 0
    
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1
        
    #method accessing class attributes
    def display_total_employees(self):
        print("Total Employees: ",Employee.employee_count)
        
    #method accessing instance attributes
    def display_employee(self):
        print(f"Employee Name: {self.name}\nEmployee salary: {self.salary}")

#creating objects of the class emplyee
employee1 = Employee("John",50000)
employee2 = Employee("Alice",40000)
employee1.display_employee()
employee2.display_employee()
employee1.display_total_employees()
print("----------------------------------")

#hasattr
print("Has attribute salary: ",hasattr(employee1, 'salary'))

#getattr
print("get attribute salary: ",getattr(employee1, 'salary'))

#setattr
setattr(employee1,'salary',30000)
print("Set attribute salary",employee1.salary)

#delattr
delattr(employee1,'salary')  
print("----------------------------------")   

#built in class attributes
print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__)
print("----------------------------------")

#deleting object
del employee1
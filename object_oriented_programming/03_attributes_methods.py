class Employee:
    #class attribute
    employee_count = 0
    
    def __init__(self,name,salary):
        self.name = name #instance attribute
        self.salary = salary #instance attribute
        Employee.employee_count += 1
        
    
    def display_total_employees(self):
        print("Total Employees: ",Employee.employee_count)
    
    #class method using classmethod()    
    counter1 = classmethod(display_total_employees)
        
    #class method using @classmethod decorator
    @classmethod
    def showcount1(cls):
        print(cls.employee_count)
        
    #instance method
    def display_employee(self): 
        print(f"Employee Name: {self.name}\nEmployee salary: {self.salary}")
    
    #static method using staticmethod()
    def showcount2():
        print(Employee.employee_count)
        return
    counter2 = staticmethod(showcount2)
    
    #static method using @staticmethod
    @staticmethod
    def showcount3():
        print(Employee.employee_count)
        return
    
emp1 = Employee("John",25000)

#accessing instance Attributes
print(emp1.name,emp1.salary)

#accessing class attributes
print(Employee.employee_count)

#accessing instance method
emp1.display_employee()

#accessing class methods
emp1.display_total_employees()
Employee.counter1()
Employee.showcount1()

#accessing static methods
emp1.counter2()
Employee.counter2()
Employee.showcount3()
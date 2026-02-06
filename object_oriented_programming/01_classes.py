#creating class
class Employee:
    #class attribute
    employee_count = 0
    
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1
        
    def display_total_employees(self):
        print("Total Employees: ",Employee.employee_count)
        
    def display_employee(self):
        print(f"Employee Name: {self.name}\nEmployee salary: {self.salary}")
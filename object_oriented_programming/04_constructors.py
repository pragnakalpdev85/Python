#default constructor
class Employee:
   def __init__(self):
      self.name = "John"
      self.age = 24

emp1 = Employee()
print (f"Name: {emp1.name}")
print (f"age: {emp1.age}")

#Parameterized Constructor
class Employee:
    def __init__(self,name,age):
       self.name = name
       self.age = age
       
emp2 = Employee("Alice",35)
print (f"Name: {emp2.name}")
print (f"age: {emp2.age}")

#deafault values in constructor
class Employee:
    def __init__(self,name,age = 20):
       self.name = name
       self.age = age
       
emp3 = Employee("Bob")
print (f"Name: {emp3.name}")
print (f"age: {emp3.age}")

#multiple constructors
class Employee:
   def __init__(self, *args):
      if len(args) == 1:
         self.name = args[0]
        
      elif len(args) == 2:
         self.name = args[0]
         self.age = args[1]
        
      elif len(args) == 3:
         self.name = args[0]
         self.age = args[1]
         self.gender = args[2]
            
emp4 = Employee("John")
print("Name:", emp4.name)
emp5 = Employee("Alice", 25)
print(f"Name: {emp5.name} and Age: {emp5.age}")
emp6 = Employee("Bob", 26, "M")
print(f"Name: {emp6.name}, Age: {emp6.age} and Gender: {emp6.gender}")
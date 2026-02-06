#duck typing
class Car:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        print("Drive")

class Boat:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        print("Sail")

class Plane:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        print("Fly")

car1 = Car("Ford")
boat1 = Boat("Ibiza") 
plane1 = Plane("Boeing") 
list_objects = [car1,boat1,plane1]
for object in list_objects:
    object.move()

#method overriding 
class GrandParent:
    def display(self):
        print("Grand Parent class")

class Parent(GrandParent):
    def display(self):
        print("Parent class")

class Child(Parent):
    def display(self):
        print("Child class")
        
child = Child()
parent = Parent()
grandparent = GrandParent()
child.display()
parent.display()
grandparent.display()

#operator overloading 
class Vector:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        
    def __str__(self):
        return f"Vector ({self.num1}, {self.num2})"
        
    def __add__(self,other):
        return Vector(self.num1+other.num1, self.num2+other.num2)
vec1 = Vector(2,3)
vec2 = Vector(5,-2)
print(vec1 + vec2)
        
#method overloading
def add(*nums):
    return sum(nums)

print(add(1,2))
print(add(1,2,3,4,5))

#dynamic typing
var = 25
print("Type - ",type(var),", var - ",var)
var = "Hello"
print("Type - ",type(var),", var - ",var)
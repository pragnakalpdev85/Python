from dataclasses import dataclass, field, asdict
from typing import List 

#without dataclass
class Student:  
    def __init__(self, name: str, age: int, percent: float):  
        self.name = name  
        self.age = age  
        self.percent = percent  
    def __repr__(self):  
        return f"Student(name={self.name}, age={self.age}, percent={self.percent})"  
    def __eq__(self, other):  
        if not isinstance(other, Student):  
            return NotImplemented  
        return (self.name == other.name and self.age == other.age and self.percent == other.percent)
    
#with data class
@dataclass  
class Student:  
    name: str  
    age: int  
    percent: float

s1 = Student("Alice", 20, 90.0)
s2 = Student("Bob", 22, 85.5)

print(s1)         
print(s1 == s2)

#data class with mutable default values

@dataclass
class Course:
    name: str
    students: List[str] = field(default_factory=list)  # Mutable default value

course1 = Course("Math")
course2 = Course("Science", ["Alice", "Bob"])
course1.students.append("Charlie")
print(course1)
print(course2)

#Setting Up Post-Initialization
@dataclass
class Rectangle:
    width: float
    height: float
    area: float = 0.0  # This will be calculated in __post_init__

    def __post_init__(self):
        self.area = self.width * self.height  # Calculate area after initialization
r = Rectangle(5.0, 10.0)
print(r)
print(f"Area of the rectangle: {r.area}")

#convert data class into dictionary
@dataclass
class Student:
    name: str
    age: int
    grades: List[float]  

student = Student("Alice", 20, [88.5, 92.0, 79.5])
student_dict = asdict(student)
print(student_dict)
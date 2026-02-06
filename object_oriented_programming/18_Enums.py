from enum import Enum

#Enums
class Subjects(Enum):
   ENGLISH = 1
   MATHS = 2
   SCIENCE = 3
   SANSKRIT = 4

obj = Subjects.MATHS
print(obj)
print (type(obj))

subjects = Enum("subjects","MATHS SCIENCE ENGLISH")
obj = subjects.ENGLISH
print(obj)
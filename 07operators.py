#operators

#arithmetic operators
print("addition: 10+10=",10+10) 
print("subtraction: 5-2=",5-2) 
print("multiplication: 5*5=", 5*5)
print("division: 5/2=", 5/2)
print("division: 5//2=", 5//2)
print("modulas: 5%2=",5%2)
print("exponential: 5^2=",5**2)

#assignment operators
a = 10
print(a)
a += 10
print(a)
a-=5
print(a)
a/=3
print(a)
a*=10
print(a)

#comparision operators
print(a == 50)
print(a != 20)
print(a > 10)
print(a < 100)

#logical operator
print(a > 10 and a < 55)
print(a > 50 or a > 45)
print(not True)

#identity operator
a = [1,2]
b = [1,2]
c = a
print(a == b)
print(a is c)
print(a is b)

#MEMBERSHIP OPERATOR
print(2 in b)

#bitwise operators
print(6 & 3)
print(6 | 3)
print(6 ^ 3)
print(6 << 2)
print(6 >> 2)
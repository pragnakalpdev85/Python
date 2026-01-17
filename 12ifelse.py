#input is greater or less than 10
num1 = int(input("enter a number: "))
if(num1 > 10):
    print("a is greater than 10")
else:
    print("a is less than 10")

#taking input and checking the number is odd or even
num2 = int(input("enter a number: "))
if(num2%2 == 0):
    print("it is an even number")
else:
    print("it is an odd number")

#check the given number is prime or not
num3 = int(input("enter a number: "))
flag = True
if(num3 == 1 or num3 == 0): flag = False
for i in range(2,num3//2):
    if(num3%i):
        flag = False
        break
if(flag == True):
    print("number is prime")
else:
    print("number is not prime")
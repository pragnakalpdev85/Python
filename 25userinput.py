#taking input and printing input value and default type of input
print("enter any value")
input1 = input()
print(input1," : default type of input: ",type(input1))
#using prompt parameter
input2 = input("enter any value: ")
print(input2," : default type of input: ",type(input2))

#taking input in different data types
intinput = int(input("enter a number: "))
floatinput = float(input("enter a number with decimal: "))
strinput = str(input("enter a string: "))
boolinput = bool(input("enter a boolean: "))
print(f"integer as input : {intinput} , type: {type(intinput)}")
print(f"float as input : {floatinput} , type: {type(floatinput)}")
print(f"string as input : {strinput} , type: {type(strinput)}")
print(f"boolean as input : {boolinput} , type: {type(boolinput)}")

#taking multiple values as input
a, b, c = map(int,input("enter 3 numbers: ").split())
print(f"number 1: {a}\nnumber 2: {b}\nnumber 3: {c}")

#taking list as input
l = list(input("enter list elements: ").split())
print(l)
#taking list of numbers as input
numlist = list(map(int,input("enter numbers: ").split()))
print(numlist )

#taking tuple as input
t = tuple(input("enter tuple elements: ").split())
print(t)

#taking set as input
s = set(input("enter set elements: ").split())
print(s)

#taking dictionary as input
d = eval(input("enter dictionary: "))
print(d,type(d))
#another method for taking dictionary as input
d = {}
n = int(input("enter the number of key-value pairs: "))
for i in range(n):
    key = input("enter key: ")
    value = input("enter value: ")
    d[key] = value
print(d)
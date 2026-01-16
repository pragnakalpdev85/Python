#creating and calling a function with parameters
def sum(num1, num2):
    return num1 + num2

print(sum(1,2))
print(sum(22,556))

#pass statement
def empty_func():
    pass

#arbitrary arguments
#returns first and last argument
def arb_args(*para):
    return f"first argument is {para[0]} and last one is {para[-1]}"

#returns sum of all arguments
def sum_of_all(*nums):
    total = 0
    for i in nums:
        total += i
    return total

print(arb_args("a","b","c","d"))
print(sum_of_all(1,2,3,4,5))

#**kwargs parameter
def user_details(**userdata):
    print("name: ",userdata["name"])
    print("role number: ",userdata["roleno"])

def user_details2(name, roleno):
    print("name: ",name)
    print("role number: ",roleno)

user = {"name" : "het",
        "roleno" : 50 }

user_details(name = "het", roleno = 50)
user_details2(**user)

#scope and keywords
#global keyword
def global_keyword():
    global num1
    num1 = 10001
    print(num1)
global_keyword()
print(num1)

#nonlocal keyword
def nonlocal_demo():
    x = 1000
    def inner_func():
        nonlocal x
        x += 100
    inner_func()
    print(x)

nonlocal_demo()

#lambda functions
sumoftwo = lambda a,b : a+b
print(sumoftwo(11,22))

multiply = lambda a,b : a*b
print(multiply(4,4))

#recursion
def fib1(n):
    if(n <= 1): return n
    else:
        return fib1(n-1) + fib1(n-2)

print(fib1(10))

#generator
def genrate_even_count(n):
    count = 0
    while count <= n:
        yield count
        count += 2

for i in genrate_even_count(20):
    print(i)

#decorators
def increase_10persent(func):
    def innner(num):
        return func(num+num%10)
    return innner

@increase_10persent
def imple(num):
    return f"incresed number by 10 persent is {num}"

print(imple(55))



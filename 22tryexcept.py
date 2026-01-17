#try and axcept
try:
    print(a) # type: ignore
except NameError:
    print("variable a is undefined")
except:
    print("something went wrong")

#else 
a = 20
try:
    print(a)
except:
    print("something went wrong")
else:
    print("everything is OK")

#finally
try:
    num = int(input("enter a number: "))
except:
    print("something went wrong")
finally:
    print("operation 1 is over")

#raise an exception
def exception(n):
    if(n < 0): raise Exception("number is not valid for operation")
    else: print(n+5555)

try:
    exception(-55)
except Exception as e:
     print(e)
finally:
    print("operation 2 is over")

#raise typeError
def type_error(n):
    if not type(n) is int:
        raise TypeError("enter an integer")

try:
    type_error("hello")
except TypeError as e:
     print(e)
finally:
    print("operation 3 is over")
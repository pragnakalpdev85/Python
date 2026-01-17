#None
varnone = None
print(varnone)
print(type(varnone))

#boolean of None
print(bool(varnone))

#using None in conditional statements
if(varnone is None):
    print("variable has None value")
else:
    print("variable has some value")

var = 22

if(var is not None):
    print("variable has value")
else:
    print("variable has None value")

#function returning none
def print_string():
    print("hello world")

varnone = print_string()
print(varnone, type(varnone))
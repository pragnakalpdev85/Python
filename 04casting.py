#casting

#integer casting
int1 = int(4.25)
int2 = int("55")
int3 = int(25)
print(f"{type(int1)}: {int1}\n{type(int2)}: {int2}\n{type(int3)}: {int3}\n") 

#float casting
float1 = float(55)
float2 = float("99.99")
float3 = float(1)
print(f"{type(float1)}: {float1}\n{type(float2)}: {float2}\n{type(float3)}: {float3}")

#string casting
str1 = str(25)
str2 = str(25.222)
str3 = str({"name":"het"})
print(f"{type(str1)}: {str1}\n{type(str2)}: {str2}\n{type(str3)}: {str3}")

#casting integer to string
x = 10000
y = str(x)
print(y ,"- type: ",type(y))

#casting bool to string
z = str(True)
print(z ,"- type: ",type(z))

#casting string into integer
a = int("3")
print(a, "- type: ",type(a))

#casting String into bool
b = bool("True")
print(b, "- type: ",type(b))
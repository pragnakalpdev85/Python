import random

#numeric types in python
#integer
int1 = 5
int2 = -5
int3 = -545413516
print(f"{type(int1)}: {int1}\n{type(int2)}: {int2}\n{type(int3)}: {int3}\n") 

#float
float1 = 22.22
float2 = -2.777945112
float3 = 1.00
float4 = 12e4
float5 = 3E3
float6 = -35.66e10
print(f"{type(float1)}: {float1}\n{type(float2)}: {float2}\n{type(float3)}: {float3}")
print(f"{type(float4)}: {float4}\n{type(float5)}: {float5}\n{type(float6)}: {float6}\n")  

# complex
complex1 = 1j 
complex2 = 3+4j
complex3 = -5j
print(f"{type(complex1)}: {complex1}\n{type(complex2)}: {complex2}\n{type(complex3)}: {complex3}\n") 


#generating random number from 0-9
randomnum = random.randrange(0,9)
print("generated random number: ",randomnum)
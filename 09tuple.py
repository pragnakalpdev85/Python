#tuples
tuple1 = (1,2,3)
print(tuple1,"- type: ", type(tuple1))

#slicing in tuple
print(tuple1[:1])

#looping through tuple
for i in tuple1:
    print(i)

#join tuple
tuple2 = (4,5,6,6,6,6)
print(tuple1+tuple2)

#count occurence
print(tuple2.count(6))

#finding first occurence of element
print(tuple2.index(6))

#manipulating tuple
x = list(tuple1)
x.append(10)
tuple1 = tuple(x)
print(tuple1)

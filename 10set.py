#set
set1 = {1,4,5,8,6,9}
print(set1, "-type: ",type(set1))

#accessing elements of set
for i in set1:
    print(i)

#check the element is present or not
print(4 in set1, 7 in set1)

#adding elements
set1.add(7)
set1.update({11,12,13,14})
print(set1)

#removing element from set
set1.remove(11)
print(set1)

#union,intersection and diffrence methods
set2 = {8,9,10,11,12,13,14,15,16,17}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
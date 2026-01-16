#list
list1 = ["apple", "banana", "watermelon", "banana", "cherry"]
print(list1)

#length of the list 
print("length of the list: ", len(list1))

#list using constructor
newlist = list((1,2,3,4,5))
print(newlist)

#slicing in list
print(list1[2:4])
print(list1[::-1])
print(list1[:3])

#access list elements
print(list1[0])
print(list1[2])

#adding elements to the list
list1.append("apple")
list1.insert(2,"apple")
print(list1)

#remove element from the list
list1.remove("apple")
print(list1)

#looping through list
for i in list1:
    print(i)

#List comprehension
newlist1 = [x.upper() for x in list1 if x == "apple"]
print(newlist1)

#sort
newlist.sort(reverse=True)
print(newlist)

#copying list
newlist2 = newlist1.copy()
print(newlist2)

#join two list
print(newlist1+newlist2)

#clearing out the list elements
newlist2.clear()
print(newlist2)

#dictionary
dict1 = {
    "name" : "het",
    "enrollment" : 50,
    "DOB" : "26 may 2000"}
print(dict1,"-type: ",type(dict1))
print(dict1["name"])
print(len(dict1))

#changing dictionary elements
dict1["DOB"] = "2 jan 2000"
dict1.update({"bloodgroup" : "O+"})
print(dict1)

#coping dictionary
dict2 = dict1.copy()
print(dict2)

#loop through dictionary
for i in dict1:
    print(dict1[i])

#printing only keys
print(dict1.keys())

#printing out values
print(dict1.values())

#printing all elements with key and values
print(dict1.items())

#remove
dict1.pop("bloodgroup")
print(dict1)
dict1.popitem()
print(dict1)
dict1.clear()
print(dict1)
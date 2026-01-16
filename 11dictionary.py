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

#nested dictionary
cars = {
    "car1":{
        "name": "thar",
        "model": 2022
    },
    "car2":{
        "name":"scorpio",
        "model": 2025
    }
}

#printing out nested dictionari
for i,obj in cars.items():
    print(i," : ")
    for k in obj:
        print("  ",k," : ",obj[k])

#accessing element from nested dictionary
print(cars["car1"]["name"])

#removing element using pop in nested dictionary
cars["car1"].pop("name")
print(cars)

#removing element from nested dictionary using popitems
cars["car1"].popitem()
print(cars)

#adding element to the nested dictionary
cars["car1"]["name"] = "thar"
print(cars)

#clearing out all data from dictionary using clear()
cars.clear()
print(cars)


#creating resource to export
person = {
    "name" : "het",
    "rolno" : 50,
    "gender" : "male"
}

def print_data(person):
    for i in person:
        print(i,": ",person[i])
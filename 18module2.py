#importing module and accessing other modules resources
import module1

print(module1.person["name"])
print(module1.person)
person = {
    "name" : "het",
    "rolno" : 50,
    "gender" : "male"
}
module1.print_data(person)

print(dir(module1))


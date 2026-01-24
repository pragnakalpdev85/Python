import json

data = {
    "name" : "Het Patel",
    "age" : 25,
    "city" :"chikhli"
}

#converting dictionary to json string 
json_string1 = json.dumps(data)
print(type(json_string1) ,' : ',json_string1)

#converting dictionary to json string with indent
json_string2 = json.dumps(data,indent=4)
print(json_string2)

#converting dictionary to json string with custom indentation and sepration
json_string3 = json.dumps(data,indent=4,separators=("."," = "))
print(json_string3)

#Sort keys alphabetically
json_string4 = json.dumps(data,indent=4,sort_keys=True)
print(json_string4)

#converting json string into python object
json_string4 = '{"name": "Het patel", "age": 25, "qualification": "BE IT"}'
data_dict1 = json.loads(json_string4)
print(type(data_dict1), " : ",data_dict1)

#type conversion
json_string5 = '''
{
    "string": "Hello world",
    "number": 999,
    "float": 22.22,
    "boolean": true,
    "null_value": null,
    "array": [0, 3, 6],
    "object": {"object-1": "value-1"}
}
'''
data_dict2 = json.loads(json_string5)
print(f"String: {data_dict2['string']} - {type(data_dict2['string'])}")  # str
print(f"Number: {data_dict2['number']} - {type(data_dict2['number'])}")  # int
print(f"Float: {data_dict2['float']} - {type(data_dict2['float'])}")  # float
print(f"Boolean: {data_dict2['boolean']} - {type(data_dict2['boolean'])}")  # bool
print(f"Null: {data_dict2['null_value']} - {type(data_dict2['null_value'])}")  # NoneType
print(f"Array: {data_dict2['array']} - {type(data_dict2['array'])}")  # list
print(f"Object: {data_dict2['object']} - {type(data_dict2['object'])}")  # dict




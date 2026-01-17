import json

#json string
jsontext = '{"name":"Het","age":21,"gender":"male"}'

#load json string
obj1 = json.loads(jsontext)
print(obj1)
print(type(obj1))
for i in obj1:
    print(i,": ",obj1[i])

#converting different datatypes into json
print(json.dumps({"name":"Het","age":21,"gender":"male"}))
print(json.dumps([1,2,3,4,5,6,7,8,9,10]))
print(json.dumps((1,2,3,4,5,6,7,8,9,10)))
print(json.dumps("hello world"))
print(json.dumps(42))
print(json.dumps(42.22))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#adds indent in string
print(json.dumps(obj1,indent=1))

#separator to change default separators
print(json.dumps(obj1, indent=1, separators=(". "," = ")))

#sort keys
print(json.dumps(obj1, indent=1, separators=(". "," = "), sort_keys=True))
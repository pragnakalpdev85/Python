import json

#json string with extra comma
json_string1 = '{"name": "John", "age": 30,}'

json_string2 = '{"name": "John", "age": 30}'

#handling error 
try: 
    json.loads(json_string1)
except json.JSONDecodeError as e:
    print("Invalid json String, ",e)
except Exception as e:
    print(e)

#safely loading json
def load_json(json_string):
    try: 
        json.loads(json_string)
        print(json_string)
    except json.JSONDecodeError as e:
        print("Invalid json String, ",e)
    except Exception as e:
        print(e)

load_json('{"name":"het"}')
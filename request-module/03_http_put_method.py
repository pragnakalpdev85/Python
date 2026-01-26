import requests

data = {
    "name" : "het",
    "age" : 29,
    "gender" : "male"
}

url = "https://httpbin.org/put"

response = requests.put(url,data)

#response status code and response data
print(f"Status code: {response.status_code}\n")
print(f"Updated data : {response.json()['form']}\n")
print(f"json : {response.json()}\n")




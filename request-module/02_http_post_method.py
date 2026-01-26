import requests

data1 = {
    "name" : "het",
    "age" : 29,
    "gender" : "male"
}

url = "https://httpbin.org/post"

#post request
response = requests.post(url,data1)

#response status code and response data
print(f"Status code: {response.status_code}")
print(f"data : {response.json()['form']}\n")

data2 = {
    "username" : "Random1234",
    "password" : "abc@1234"
}

url = "https://httpbin.org/post"

#post request
response = requests.post(url,data2)

#response status code and response data
print(f"Status code: {response.status_code}")
print(f"data : {response.json()['form']}")


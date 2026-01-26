import requests

url = "https://httpbin.org/get"

#simple get request
response = requests.get(url)

#printing the response data if status code is 200
if response.status_code == 200:
    print("Success!")
    data = response.json()
    print(f"Data: {data}\n")
else:
    print(f"Failed. Status code: {response.status_code}\n")

print(f"Status Code: {response.status_code}\n")
print(f"Headers: {response.headers}\n")
print(f"Encoding: {response.encoding}")
print(f"Content (raw bytes): {response.content[:100]}\n")
print(f"Text (decoded): {response.text[:100]}\n")
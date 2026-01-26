import requests

url = "https://httpbin.org/delete"

#deleting resource
response = requests.delete(url)
print(response.json())
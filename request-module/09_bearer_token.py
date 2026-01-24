import requests

headers = {
    'Authorization': 'Bearer mytoken2652456'
}

response = requests.get('https://httpbin.org/bearer', headers=headers)

print("status code: ",response.status_code)
print(response.json())
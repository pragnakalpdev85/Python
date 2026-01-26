import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Custom Bot)',
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer Mytoken12345'
}

#custom headers
response = requests.get('https://httpbin.org/headers', headers=headers)
print("Headers: ",response.json()['headers'])
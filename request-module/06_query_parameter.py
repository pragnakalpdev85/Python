import requests

# Passing query parameters (e.g., ?page=2&limit=10)
payload = {
    'page': 2,
    'limit': 10,
    'sort': 'desc'}
response = requests.get('https://httpbin.org/get', params=payload)

print("Query parameters: ",response.json()['args'],"\n")
print("Response: ",response.json())
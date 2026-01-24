import requests

# Method 1: As query parameter
params = {'api_key': 'het-apikey'}
response = requests.get('https://httpbin.org/get', params=params)

print("status code: ",response.status_code)
print(response.json())

# Method 2: As header
headers = {'X-API-Key': 'het-apikey'}
response = requests.get('https://httpbin.org/headers', headers=headers)

print("status code: ",response.status_code)
print(response.json())
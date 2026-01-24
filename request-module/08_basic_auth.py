from requests.auth import HTTPBasicAuth
import requests

# Method 1: Using tuple
response = requests.get(
    'https://httpbin.org/basic-auth/user/passwd',
    auth=tuple(('user', 'passwd'))
)

print("status code: ",response.status_code)
print(response.json(),"\n")

# Method 2: Using HTTPBasicAuth explicitly
response = requests.get(
    'https://httpbin.org/basic-auth/user/passwd',
    auth=HTTPBasicAuth('user', 'passwd')
)

print("status code: ",response.status_code)
print(response.json())
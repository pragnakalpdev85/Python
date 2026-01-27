import requests

# automatic JSON encoding
data = {'key': 'value', 'number': 42}
response = requests.post('https://httpbin.org/post', json=data)
print(response.json(),'\n')

# automatic JSON decoding
response = requests.get('https://httpbin.org/json')
if response.headers.get('Content-Type') == 'application/json':
    data = response.json()
    print(data)

# handle JSON decode errors
try:
    data = response.json()
except requests.exceptions.JSONDecodeError:
    print("Response is not valid JSON")
    print(f"Raw response: {response.text}")
import requests

# Adding custom headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Custom Bot)',
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer My_TOKEN'
}

response = requests.get('https://jsonplaceholder.typicode.com/posts', headers=headers)
print(response.headers['Content-Type'])
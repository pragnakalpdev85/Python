import requests

# Passing query parameters (e.g., ?page=2&limit=10)
params = {
    'page': 2,
    'limit': 10,
    'sort': 'desc'
}
response = requests.get('https://jsonplaceholder.typicode.com', params=params)
print(f"Full URL: {response.url}")
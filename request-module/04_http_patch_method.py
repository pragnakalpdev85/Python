import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'
partial_update = {
    'title': 'New Title Only'
}

#parcially updating resources
response = requests.patch(url, json=partial_update)
print(f"Patched: {response.json()}")
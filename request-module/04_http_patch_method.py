import requests

url = "https://httpbin.org/patch"

partial_update = {
    'title': 'New Title Only'
}

#partially updating data 
response = requests.patch(url, json=partial_update)
print(f"Patched: {response.json()}")
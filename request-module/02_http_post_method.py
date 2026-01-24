import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    'title': 'Demo for http post method',
    'body': 'This is the content of the post.',
    'userId': 1
}

response = requests.post(url,json = payload)
print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")
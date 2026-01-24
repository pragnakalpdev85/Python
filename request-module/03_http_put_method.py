import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'
updated_data = {
    'id': 1,
    'title': 'Title is updated',
    'body': 'Content is Updated',
    'userId': 1
}

#updating existing resource
response = requests.put(url, json=updated_data)
print(f"Updated: {response.json()}")
import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'

#deleting resource
response = requests.delete(url)
print(f"Deleted. Status: {response.status_code}")
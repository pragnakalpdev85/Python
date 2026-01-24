import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

#get request
response = requests.get(url)

if response.status_code == 200:
    print("success")
    data = response.json()
    print(f"Title: {data['title']}")
    print(f"Body: {data['body']}\n")
else:
    print(f"Failed. Status code: {response.status_code}\n")

# access response properties
print(f"Status Code: {response.status_code}\n")
print(f"Headers: {response.headers}\n")
print(f"Encoding: {response.encoding}\n")
print(f"Content (raw bytes): {response.content[:100]}\n")
print(f"Text (decoded): {response.text[:100]}\n")


          

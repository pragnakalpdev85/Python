import requests

#creating session
session = requests.Session()

# Set default headers for all requests in this session
session.headers.update({
    'User-Agent': 'New App',
    'Authorization': 'Bearer het-tokenabc'
})

# All requests will now use these headers
response1 = session.get('https://httpbin.org/headers')
response2 = session.get('https://httpbin.org/headers')

print(f"resopnse 1 headers: user-agent = {response1.json()['headers']['User-Agent']}, Authorization = {response1.json()['headers']['Authorization']}\n")
print(f"resopnse 2 headers: user-agent = {response1.json()['headers']['User-Agent']}, Authorization = {response2.json()['headers']['Authorization']}\n")

# Login example
session = requests.Session()
login_data = {'username': 'user', 'password': 'pass'}
response3 = session.post('https://httpbin.org/post', data=login_data)

print("login data resoponse: ",response3.status_code)
print("login response : ",response3.json(),"\n")

# Close session when done
session.close()

# Or use context manager (recommended)
with requests.Session() as session:
    session.headers.update({
        'User-Agent': 'New App',
        'Authorization': 'Bearer het-tokenabc'
    })
    response = session.get('https://httpbin.org/headers')
    print("response : ",response.json())
    # Session automatically closed after this block
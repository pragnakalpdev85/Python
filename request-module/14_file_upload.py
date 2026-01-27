import requests

# Upload a single file
files1 = {'file': open('document.txt', 'rb')}
response1 = requests.post('https://httpbin.org/post', files=files1)
print(response1.json(),'\n')

# Upload with additional form data
files2 = {'file': open('document.txt', 'rb')}
data = {'description': 'My document', 'tags': 'text'}
response2 = requests.post('https://httpbin.org/post', files=files2, data=data)
print(response2.json(),'\n')

#upload multiple files
files = {
    'file1' : open('document.txt', 'rb'),
    'file2' : open('/home/pragnakalpl24/Downloads/Python/Python/request-module/document.txt', 'rb')
}
response3 = requests.post('https://httpbin.org/post', files=files)
print(response3.json(),'\n')

#Using context manager to ensure files are closed
with open('document.txt', 'rb') as file:
    file = {'file' : file}
    response4 = requests.post('https://httpbin.org/post', files=file)
    print(response4.json())


import requests

# Set timeout (in seconds)
#10 sec delay and timeout is set to 5 sec
try:
    # Timeout for connection and read
    response = requests.get('https://httpbin.org/delay/10', timeout=5)
except requests.exceptions.Timeout:
    print("Request timed out!")

#time out is set to 5 sec and delay is 2 sec
try:
    # Timeout for connection and read
    response = requests.get('https://httpbin.org/delay/2', timeout=5)
    print(response.json(),"\n")
except requests.exceptions.Timeout:
    print("Request timed out!")

try:
    # (connect timeout, read timeout)
    response = requests.get('https://httpbin.org/delay/20', timeout=(3, 10))
except requests.exceptions.Timeout:
    print("Request timed out!")
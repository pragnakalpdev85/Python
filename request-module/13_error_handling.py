import requests
from requests.exceptions import (
    HTTPError,
    ConnectionError,
    Timeout,
    RequestException
)

url = 'https://httpbin.org/get'

try:
    response = requests.get(url, timeout=5)
    
    # Raise an exception for 4xx and 5xx status codes
    response.raise_for_status()
    
    # Process successful response
    data = response.json()
    print(data)
    
except HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")  # 404, 500, etc.
    
except ConnectionError as conn_err:
    print(f"Connection error occurred: {conn_err}")
    
except Timeout as timeout_err:
    print(f"Timeout error occurred: {timeout_err}")
    
except RequestException as req_err:
    print(f"An error occurred: {req_err}")
    
except Exception as err:
    print(f"Unexpected error: {err}")
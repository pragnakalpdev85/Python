import requests
from tqdm import tqdm

#download a file
url = 'https://httpbin.org/gzip'
response = requests.get(url)
print(response.json())

#Save to file
with open('downloaded_file.zip', 'wb') as f:
    f.write(response.content)

# For large files, use streaming to avoid memory issues
response2 = requests.get(url, stream=True)

with open('downloaded_file.zip', 'wb') as f:
    for chunk in response2.iter_content(chunk_size=8192):
        f.write(chunk)

# Download with progress tracking
response = requests.get(url, stream=True)
total_size = int(response.headers.get('content-length', 0))

with open('file.zip', 'wb') as f, tqdm(
    total=total_size,
    unit='B',
    unit_scale=True
) as pbar:
    for chunk in response.iter_content(chunk_size=8192):
        f.write(chunk)
        pbar.update(len(chunk))
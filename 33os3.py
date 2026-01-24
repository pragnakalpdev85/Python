import os
import time

path = './os-demo/new_name.txt'

#check if path exists
if os.path.exists(path):
    print("Pathe Exists ",path,"\n")

#check type
if os.path.isfile(path):
    print("It is a file\n")
elif os.path.isdir(path):
    print("It is a directory\n")
elif os.path.islink(path):
    print("It is a symbolic link\n")

# Get file size (in bytes)
if os.path.isfile(path):
    size = os.path.getsize(path)
    print(f"File size: {size} bytes ({size / 1024:.2f} KB)\n")

# Get last modification time (timestamp)
modification_time = os.path.getmtime(path)
read_time = time.ctime(modification_time)
print(f"Last modified: {read_time}\n")

# Get creation time
created_time = os.path.getctime(path)
print(f"Created: {time.ctime(created_time)}\n")

# Get last access time
access_time = os.path.getatime(path)
print(f"Last accessed: {time.ctime(access_time)}\n")
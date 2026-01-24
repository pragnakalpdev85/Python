import os
import shutil
import subprocess
import time

# Remove a file
if os.path.exists('./new_file.txt'):
    os.remove('./new_file.txt')
    print("File removed")

# Remove an empty directory
if os.path.exists('./new_folder'):
    os.rmdir('./new_folder')
    print("Empty directory removed")

# To remove a non-empty directory, use the shutil module
if os.path.exists('./new_folder1'):
    shutil.rmtree('./new_folder1')
    print("Directory tree removed")

# Access all environment variables (returns a dict-like object)
print(os.environ,"\n")

# Get user environment variable
user = os.environ.get('USER') 
print(f"Current User: {user}\n")

# Using os.getenv() allows a default value
api_key = os.getenv('API_KEY', 'default_key_if_none')
print(f"API Key: {api_key}\n")

# Set an environment variable
os.environ['MY_VAR'] = 'myvalue'
print(f"MY_VAR: {os.getenv('MY_VAR')}\n")

#exicuting shell command
exit_code = os.system('echo "Hello from shell"')
print(f"Command exit code: {exit_code}\n")

# Better approach with subprocess
result = subprocess.run(['echo', 'Hello from shell'], capture_output=True, text=True)
print(f"Output: {result.stdout}")
print(f"Error: {result.stderr}")
print(f"Return code: {result.returncode}\n")

# Get detailed file statistics
if os.path.exists('./os-demo/new_name.txt'):
    stats = os.stat('./os-demo/new_name.txt')
    print(f"Size: {stats.st_size} bytes")
    print(f"Mode: {oct(stats.st_mode)}")
    print(f"UID: {stats.st_uid}")
    print(f"GID: {stats.st_gid}")
    print(f"Modified: {time.ctime(stats.st_mtime)}")

# Check if file is readable/writable/executable
if os.access('./os-demo/new_name.txt', os.R_OK):
    print("File is readable")
if os.access('./os-demo/new_name.txt', os.W_OK):
    print("File is writable")
if os.access('./os-demo/new_name.txt', os.X_OK):
    print("File is executable")
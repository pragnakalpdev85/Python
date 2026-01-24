import os

#Join path safely
full_path =  os.path.join(os.getcwd(), 'new_folder', 'file.txt')
print(f"constructed path: {full_path}\n")

# Split path into directory and filename
directory, filename = os.path.split(full_path)
print(f"Directory: {directory},\nFile: {filename}\n")

# Split filename into name and extension
name, extension = os.path.splitext(filename)
print(f"Name: {name}, Extension: {extension}\n")

# Get absolute path
abs_path = os.path.abspath('./os-demo/new_name.txt')
print(f"Absolute Path: {abs_path}\n")


#Get directory name from path
dirname = os.path.dirname(full_path)
print(f"Directory Name: {dirname}\n")

# Get base filename from path
basename = os.path.basename(full_path)
print(f"Base Name: {basename}\n")

# Expand user home directory
home_path = os.path.expanduser('~/os-demo/new_name.txt')
print(f"Expanded Path: {home_path}")
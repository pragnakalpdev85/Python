import os

#Get the current working directory
cwd = os.getcwd()
print(f"Current Directory: {cwd}\n")

#change the working directory
os.chdir('/home/pragnakalpl24/Downloads/Python/Python/os-demo')
print("Current Directory: ",os.getcwd(),"\n")

#changing back to original directory
os.chdir(cwd)
print(f"Current directory: {os.getcwd()}\n")

#List all files and directories in current path 
files = os.listdir(".")
print("Files and Folders in current Directory: ",files,"\n")

#List all files and directories in given path 
files = os.listdir("/home/pragnakalpl24/Downloads/Python/Practice-questions")
print("Files and Folders in given Directory: ",files,"\n")

#Filter Only files or only directories
path = '.'
all_items = os.listdir(path)
files = [f for f in all_items if os.path.isfile(os.path.join(path,f))]
dirs = [d for d in all_items if os.path.isdir(os.path.join(path, d))]

print(f"Files: {files}")
print(f"Directories: {dirs}\n")

#os.walk() recurively traverses directories
for root, dirs, files in os.walk('/home/pragnakalpl24/Downloads/Python/Practice-questions'):
    print(f"Current Directory: {root}")
    print(f"Subdirectories: {dirs}")
    print(f"Files: {files}")
    print("-" * 40)

#create a single directory
if not os.path.exists('/home/pragnakalpl24/Downloads/Python/Practice-questions/new_folder'):
    os.mkdir('new_folder')
    print("\nDirectory 'new_folder' created\n")

#create nested directories (recursive)
os.makedirs('./new_forlder/new_folder2')
print("Nested directories created\n")

#rename a file or directory
os.rename('./os-demo/rename.txt','./os-demo/new_name.txt')
print("rename.txt is renamed as new_name.txt\n")
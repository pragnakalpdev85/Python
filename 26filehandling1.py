import os

#creating and write in non existing file
def create_and_write(filename,text):
    with open(filename,"x") as f:
        f.write(text)

#read from file
def read_file(filename):
    with open(filename,"r") as f:
        return f.read()
    
#erase existing data and write new data
def write_filedata(filename,text):
    with open(filename,"w") as f:
        f.write(text)

#append new text in file
def append_filedata(filename,text):
    with open(filename,"a") as f:
        f.write(text)

#delete file
def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print("File does not exists")

filename = "26demofile.txt"

text = """hello, everyone here is the file which contains text.
The goal is to manipulate the file content and other file resources.
The manipulation is going to be done from python programe."""

newtext = "\nPrograme was written on january 17."

delete_file(filename)

#create file and write data and reading the data
create_and_write(filename,text)
print(read_file(filename),"\n")

#appending new data and reading it
append_filedata(filename,newtext)
print(read_file(filename))


import os
import json

#json file handling

#create file if not existing and write data
def create_write(filename, text):
    with open(filename, "x") as f:
        json.dump(text,f,indent=2)

#read file data
def read_file(filename):
    with open(filename, "r") as f:
        text = json.load(f)
        print(text)

#erase old data and write new one
def write_data(filename, text):
    with open(filename, "w") as f:
        json.dump(text,f,indent=2)

#append data
def append_data(filename, text):
    with open(filename, "r") as f:
        oldtext = json.load(f)
        for i in text:
            oldtext[i] = text[i]
    
    write_data(filename,oldtext)

#delete data from keys
def delete_data(filename, key):
    with open(filename, "r") as f:
        text = json.load(f)
        if key in text:
            del text[key]
    with open(filename, "w") as f:
        json.dump(text,f,indent=2)

#delete file
def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print("File does not exists")

filename = "27data.json"

text = {"name":"het", "age":22, "gender":"male"}
newtext = {"qualification":"BE IT","CGPA":8.00}

create_write(filename,text)
append_data(filename,newtext)
read_file(filename)
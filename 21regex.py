import re

#starts with H
text1 = "Hello my name is Het"
x = re.search("^H",text1) 
print(x)

#finds first number used in string
text = "my apartment number is F6 next to G4"
x = re.search("[0-9]",text)
print(x)

#find if string have "number" word or not
x = re.search("number",text)
print(x)

#finding words that start with n
x = re.findall(r'\b[n][a-zA-Z]*\b',text)
print(x)

#returns all number used in string
x = re.findall("[0-9]",text)
print(x)

#can do this with special sequence
x = re.findall("\d",text)
print(x)

#returns whole string which does not contains digit
x = re.findall("\D",text)
print(x)

#spliting whole string into list of strings
x = re.split(" ",text)
print(x)

#sub method replacing the string with match 
text2 = "can we paint this picture on canvas?"
x = re.sub("can","042",text2)
print(x)

#span() method returning start and end possition of the match in tuple
x = re.search("can", text2)
print(x.span())
print(re.search("apartment",text).span())

#returning string passed into the function
print(x.string)

#printing the matched part of string using group() method
print(x.group())

text3 = "My name is Het Sanjakumar Patel"
x = re.findall(r'\b[A-Z][a-zA-Z]*\b',text3)
print(x)
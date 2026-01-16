#single line string
str1 = "hello"

#multiline string
str2 = """hello,
i am het"""

#print single and multiline string and its length
print(str1, "- length: ",len(str1), "\n",str2,  "- length: ",len(str2))

#checking het is present in string or not
print("het" in str2)

#slicing str1 ffrom index 2 to 5
print(str1[2:5])

#reversing string using slicing
print(str1[::-1])

#slicing to end from index 2
print(str1[2:])

#slicing till index 4 from start
print(str1[:4])

#modify string
#to uppercase
print(str1.upper())

#to lowecase
print(str1.lower())

str3 = "hii"
str4 = "hello"
#concatinating 2 strings
print(str3+str4)

#fromating string
a = 25
print(f"the number is {a}")


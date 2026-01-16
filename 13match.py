#match
num = int(input("enter a number: "))

match num:
    case 0:
        print("number is 0")
    case 1:
        print("numer is 1")
    case 2:
        print("number is 2")
    case 3: 
        print("number is 3")
    case _:
        print("number is either below 0 or greater than 3")
# Simple Condition Check --> Boolean
# 5 > 2 --> True
# 2 > 5 --> False
if 5>2:
    print("5 is greater than 2")
    print("next statement")  # IndentationError: unindent does not match any outer indentation level 
# print("5 is greater than 2") IndentationError: expected an indented block

# if statement
# if condition:
#     statements
num = -5
if num > 0:
    print("Positive Number")

# tell me condition to check if the given number is in range
# 10 - 20
num = 12
if num>=10 and num<=20:
    print(f"The given number {num} is in range")    

# if-else statement
# if condition:
#     statements
# else:
#     statements
num = -10
if num > 0:
    print("Positive Number")
else:
    print("Negative Number")

# vote app
age = 25
if age >=18:
    print("You Can Vote")
else:
    print("You Cannot Vote")

# input function demo
# name = input("Enter Your Name: ")
# age = input("Enter Your Age: ")
# print(f"Welcome: {name} your age is {age}")

# vote app dynamic
# Apply type casting
age = int(input("Enter Your Age: "))
# print(type(age))
if age >=18:
    print("You Can Vote")
else:
    print("You Cannot Vote")
# TypeError: '>=' not supported between instances of 'str' and 'int'    

# ternary operator
# value_if_true if condition else value_if_false
age = int(input("Enter Your Age: "))
vote_status = "You Can Vote" if age >=18 else "You Cannot Vote"
print(vote_status)

# elif ladder
# if condition:
#     statements
# elif condition:
#     statements
# elif condition:
#     statements
# elif condition:
#     statements
# else:
#     statements
marks = int(input("Enter Your Marks: "))
if marks>=90:
    print("A")
elif marks>=75:
    print("B")
elif marks>=60:
    print("C")
elif marks>=50:
    print("D")
else:
    print("FAIL")

# vote app with id card
has_id = False
age = int(input("Enter Your Age: "))
if age >=18:
    if has_id:
        print("You are Allowed To Voting Center")
    else:
        print("You Need An ID To Enter Voting Center")
else:
    print("You Cannot Vote")
    
# vote app with nationality
age = int(input("Enter Your Age: "))
nationality = input("Enter Your Nationality: ")
if age >=18 and nationality == "indian":
    print("You can Vote")
else:
    print("You cannot Vote")

# match-case syntax
# choice = 2
# match choice:
#     case 1:
#         print("One")
#     case 2:
#         print("Two")
#     case 3:
#         print("Three")
#     case _:
#         print("Invalid")
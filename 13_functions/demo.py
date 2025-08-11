# Without Functions
a = 10
b = 11
print(a+b)
print(a-b)
print(a*b)
print(a/b)

a = 12
b = 13
print(a+b)
print(a-b)
print(a*b)
print(a/b)

a = 20
b = 30
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print("With Functions")

# With Functions
a = 30
b = 40
def arithmetic():
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

arithmetic() 

a = 40
b = 50
arithmetic() 

a = 50
b = 60
arithmetic() 

a = 70
b = 80
arithmetic() 

print("With Parameters")

# functions with parameters
def arithmetic(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a)
    print(b)
# arithmetic() -> TypeError: arithmetic() missing 2 required positional arguments: 'a' and 'b'
# arithmetic(40) -> TypeError: arithmetic() missing 1 required positional argument: 'b'
arithmetic(10,20)
arithmetic(20,30)
arithmetic(30,40)
# Parameters defined are local to function, cannot be accessed 
# out side the function
# print(a)
# print(b)

# a & b -> parameters
# 10 & 20 -> arguments

# functions with parameters -> Positional Arguments
def arithmetic(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
arithmetic(10,20)
arithmetic(20,10)

# functions with parameters -> Positional Arguments
def login(username,password):
    if username == "ravi" and password == "pass123":
        print("Login Success")
    else:
        print("Login Failed")
# login()
# login("ravi")
# login("ravi","pass")
# login("ravi","pass123") -> Correct 
login("pass123","ravi")

# functions with parameters -> Positional Arguments
def emp_info(emp_name,emp_email,emp_location):
    print(f"Hi {emp_name}, your email is {emp_email} and your work location is {emp_location}")
emp_info("Ravi","ravi@gmail.com","hyderabad")


# functions with parameters -> Default Arguments
def emp_info(emp_name,emp_email,emp_location="hyderabad"):
    print(f"Hi {emp_name}, your email is {emp_email} and your work location is {emp_location}")
emp_info("Ravi","ravi@gmail.com")

# functions with parameters -> Default Arguments can be overridden by function passed arguments
def emp_info(emp_name,emp_email,emp_location="hyderabad"):
    print(f"Hi {emp_name}, your email is {emp_email} and your work location is {emp_location}")
emp_info("Ravi","ravi@gmail.com","pune")

# functions with parameters -> Default Arguments next all consecutive parameters
#   should be default only
# SyntaxError: non-default argument follows default argument
# def emp_info(emp_name,emp_email,emp_location="hyderabad",address):
#     print(f"Hi {emp_name}, your email is {emp_email} and your work location is {emp_location} and your actual address is {address}")
# emp_info("Ravi","ravi@gmail.com","pune","bangalore")

def emp_info(emp_name,emp_email,emp_location="hyderabad",address="india"):
    print(f"Hi {emp_name}, your email is {emp_email} and your work location is {emp_location} and your actual address is {address}")
emp_info("Ravi","ravi@gmail.com","pune","bangalore")
emp_info("Ramu","ramu@gmail.com")

# functions with parameters -> Without Keyword(Named) Arguments
def emp_info(emp_name,emp_email,emp_location="hyderabad",address="india"):
    print(f"Hi {emp_name}, your email is {emp_email} and your work location is {emp_location} and your actual address is {address}")
emp_info("ravi@gmail.com","Ravi","pune","bangalore")

# functions with parameters -> With Keyword(Named) Arguments
def emp_info(emp_name,emp_email,emp_location="hyderabad",address="india",mobile="9090"):
    print(f"Hi {emp_name}, your email is {emp_email} and your work location is {emp_location} and your actual address is {address} and mobile is {mobile}") 
emp_info(emp_email="ravi@gmail.com",emp_name="Ravi",mobile="99999999")

# functions with parameters -> Arbitrary Positional Arguments
def add_all(*numbers):
    total = 0
    for i in numbers:
        total = total + i
    print(f"Total Sum is: {total}")

add_all(1,2,3)
add_all(10,20,30,40,50,60,70,80,90,100)

# functions with parameters -> Arbitrary Keyword Arguments
def profile(**info):
    print(info)
profile(name="ravi",email="ravi@gmail.com",mobile=9989090,rating=4.5)

# functions with parameters -> Arbitrary Keyword Arguments -> by default only keys we get
def cred_trans(**trans):
    print(trans)
    total = 0
    for i in trans:
        print(i)
cred_trans(jan=1000,feb=2000,mar=3000)

# functions with parameters -> Arbitrary Keyword Arguments -> to get values
def cred_trans(**trans):
    print(trans)
    total = 0
    for i in trans:
        print(trans[i])
cred_trans(jan=1000,feb=2000,mar=3000)

# functions with parameters -> Arbitrary Keyword Arguments -> using both for some calculations
def cred_trans(**trans):
    print(trans)
    total = 0
    for i in trans:
        total = total + trans[i]
    print(f"You have done {len(trans)} and transactions total value is {total}")
cred_trans(jan=1000,feb=2000,mar=3000)


# functions with parameters -> Arbitrary Positional & Keyword Arguments -> using both for some calculations
def cred_trans(*trans,**info):
    print(trans)
    print(info)
    total = 0
    for i in trans:
        total = total + i
    print(f"Hi {info['name']}, you have done {len(trans)} transactions for a total amount of {total} ")
cred_trans(1000,2000,3000,name="ravi",email="ravi@gmail.com")
cred_trans(5000,6000,name="ramu",email="ramu@gmail.com")


# Be default functions will not give any response 
def add(a,b):
    a+b
print(add(3,4))

# With return 
def add(a,b):
    return a+b
print(add(3,4))

# Return Statement, should be the last Statement
def add(a,b):
    return a+b
    return a-b
    return a*b
print(add(3,4))

# Return Statement, you can have multiple Return Statement
def add(a,b,opr):
    if opr == '+':
        return a+b
    elif opr == '-':
        return a-b
    else:
        return "Invalid Operator"
    print("Check this statement will run")

print(add(2,3,'+'))
print(add(2,3,'-'))
print(add(2,3,'*'))

# Local Scope works inside the function
def add():
    b = 5
    c = 7
    print(b)
    print(c)
add()

# print(c) 

def add(b,c): 
    print(b)
    print(c)
add(5,7)

# Global Scope
a = 6
def add():
    b = 5
    c = 7
    print(b)
    print(c)
    print(a)
add()

# if defined in both local and global, 1st pref is local only
a = 6
def add(b,c,a):
    print(b)
    print(c)
    print(a)
add(5,7,8)

# By default it is READ ONLY 
count = 0
def increment():
    global count
    count += 1
increment()
print("Count: ",count)

# Function Composition
def add(a,b):
    return a+b

def sub(c,d,e): # (c+d)-e
    return add(c,d) - e

print(sub(3,4,5))

# check builtins
# print(dir(__builtins__))

# Without Lambda Functions
def add(a,b):
    return a+b
print(add(3,4))

# With Lambda Functions
# lambda arguments: expression
sum = lambda a,b: a+b
print(sum(5,4))

# IILE Style
print((lambda a,b: a+b) (10,20))
print((lambda a,b: a+b) (100,200))

# Without Functional Approach 
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
print(is_even(6))

# lambda arguments: expression
print((lambda n: n % 2 == 0) (5))
print((lambda n: n % 2 == 0) (4))

# Without Higher Order Functions

# Input [1,2,3,4] --> Output [1,4,9,16]
def square_list(numbers):
    squared_list = []
    for n in numbers:
        squared_list.append(n * n)
    return squared_list
print(square_list([1,2,3,4]))

# Using map for above functionality
# map(function,iterable)
# lambda arguments: expression
print(map(lambda n: n * n,[1,2,3,4]))
print(list(map(lambda n: n * n,[1,2,3,4])))

# Without filter
# Input [1,2,3,4,5,6,7,8,9,10] --> Output [2,4,6,8,10]
def even_list(numbers):
    even_numbers = []
    for n in numbers:
        if n % 2 == 0:
            even_numbers.append(n)
    return even_numbers
print(even_list([1,2,3,4,5,6,7,8,9,10]))

# Using filter for above functionality
# filter(function,iterable)
# lambda arguments: expression

print(list(filter(lambda n: n % 2 ==0,[1,2,3,4,5,6,7,8,9,10])))

# Without reduce
# Input [1,2,3,4] --> Output 24 (1*2*3*4)
def multiply_list(numbers):
    result = 1
    for n in numbers:
        result = result * n
    return result
print(multiply_list([1,2,3,4]))

# Using reduce for above functionality
# reduce(function,iterable)
# lambda arguments: expression
from functools import reduce
print(reduce(lambda x,y: x * y,[1,2,3,4,]))
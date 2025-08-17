# My custom user defined module
name = "john"
email = "john@gmail.com"

def add(a,b):
    return a+b

def sub(a,b):
    return b-a

# more dynamic - using positional
def info(name,email):
    return f"Hello {name} your email is {email}"

# more dynamic - using keyword
def info_new(name=name,email=email):
    return f"Hello {name} your email is {email}"
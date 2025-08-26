# Exception Handling

# Everything is fine, when there are no exceptions
print("Program Execution Started")
num1 = 10
num2 = 5
print(num1/num2)
print("Program Execution Completed")

print("="*50)

# Observe the behavior when there are exceptions -> handled by python
print("Program Execution Started")
num1 = 10
num2 = 0
# print(num1/num2) # ZeroDivisionError: division by zero
print("Program Execution Completed")
print("="*50)

# Observe the behavior when there are exceptions
print("Program Execution Started")
num1 = 10
num2 = 0
try:
    print(num1/num2) # ZeroDivisionError: division by zero   
except:
    print("OOPS! You Cannot Divide By Zero - https://en.wikipedia.org/wiki/Division_by_zero")
    
print("Program Execution Completed")

# Observe the behavior when there are no exceptions with try and except
print("="*50)
print("Program Execution Started")
num1 = 10
num2 = 5
try:
    print(num1/num2) 
except:
    print("OOPS! You Cannot Divide By Zero - https://en.wikipedia.org/wiki/Division_by_zero")
    
print("Program Execution Completed")
print("="*50)

# Multiple Types Of Exceptions
list_data = [1,2,'Python',0,5,6]
for i in list_data:
    try:
        print(1/i)
    except:
        print("OOPS! Something went wrong")
    # TypeError: unsupported operand type(s) for /: 'int' and 'str'
print("Program Execution Completed")
print("="*50)    

# Multiple Types Of Exceptions
import sys
list_data = [1,2,'Python',0,5,6]
for i in list_data:
    try:
        print(1/i)
    except:
        print(sys.exc_info())
        print("OOPS! Something went wrong")
    # TypeError: unsupported operand type(s) for /: 'int' and 'str'
print("Program Execution Completed")
print("="*50) 

# Multiple Types Of Exceptions
import sys
list_data = [1,2,'Python',0,5,6]
for i in list_data:
    try:
        print(1/i)
    except TypeError:
        print("OOPS! Don't divide Strings with numbers")
    except ZeroDivisionError:
        print("OOPS! Don't divide numbers with zero")
print("Program Execution Completed")
print("="*50)  

# else block -> runs if no exception
print("="*50)
print("Program Execution Started")
num1 = 10
num2 = 5
try:
    print(num1/num2) 
except:
    print("OOPS! You Cannot Divide By Zero - https://en.wikipedia.org/wiki/Division_by_zero")
else:
    print("Calculation Was Successful!!! proceeding with further steps")
finally:
    print("Program Execution Completed")
print("="*50)

# User Defined Exceptions
class AgeTooYoungError(Exception):
    pass

class NoIDError(Exception):
    pass

# age = int(input("Enter Your Age: "))
# if age < 18:
#     raise AgeTooYoungError("You must be at least 18 years old to register")
# else:
#     has_id = input("Do you have ID ? (yes/no) ")
#     if has_id != "yes":
#         raise NoIDError("You must have an ID to register") 
# print("Registration Successful!")
# print("="*50)

try:
    age = int(input("Enter Your Age: "))
    if age < 18:
        raise AgeTooYoungError
    has_id = input("Do you have ID ? (yes/no) ")
    if has_id != "yes":
        raise NoIDError
except AgeTooYoungError:
    print("You must be at least 18 years old to register")

except NoIDError:
    print("You must have an ID to register") 
else:        
    print("Registration Successful!")
finally:
    print("Exiting Application!")    
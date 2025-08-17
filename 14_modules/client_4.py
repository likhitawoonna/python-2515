# Loading Modules -> Name Shadowing
from my_module import name,email
from other_vendor_module import name,email

print(name)
print(email)

print(name)
print(email)
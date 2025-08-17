# Client program, trying to use my_module
import my_module


# client trying to give his own data
name = "krishna"
email = "krishna@gmail.com"

print(my_module.name)
print(my_module.add(20,30))
print(my_module.info(name,email))

print(my_module.info_new(name="ram",email="ram@gmail.com"))
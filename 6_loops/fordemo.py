# for loop
# for elements in sequence
#     statements

text = "Python Programming Language"
for elements in text:
    print(elements)

num = [1,2,3,4]
for elements in num:
    print(elements) 

# # Greet 
# print("Hi")
# print("Hi")
# print("Hi")
# print("Hi")
# print("Hi")
# print("Hi")
# print("Hi")
# print("Hi")
# print("Hi")

# # greet 
# for i in range(10):
#     print("Hi",i)

# default step is 1
for i in range(1,10):
    print(i)

# odd numbers in between 1 to 10
for i in range(1,10,2):
    print(i)

# even numbers in between 1 to 10
for i in range(5,100,5):
    print(i)

# default step is 1
# specify -1 for reverse order
for i in range(10,1,-1):
    print(i)
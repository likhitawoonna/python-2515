# common string representations
str1 = "hello"
print(str1)
str2 = 'hello'
print(str2)

# triple use case
str3 = '''hello'''
print(str3)

# multi lines
# poem = "some some poem
# peom poem"
poem = '''some some poem
peom poem
'''
print(poem)

# text = "Python"          P y t h o n
# Strings use indexing --> 0 1 2 3 4 5 6

# Indexing Start From Zero, goes from Left To Right
text = "Python"
print(text[0])
print(text[4])

# Indexing Can Start From -1, goes from Right To Left 
print(text[-1])
print(text[-2])

# Index out of range
# print(text[10])

# access multiple characters
# print(text[123])

# String Slicing
# string(start:stop:step)
print(text[0:3]) # 0 to 2
print(text[1:4]) 
print(text[2:5]) 

print(text[:5])
print(text[:])

text = "pythin is very easy to learn"
print(text[1:10:1])
print(text[1:10:2])
print(text[1:10:3])

text = "Python"
print(text[-1])
print(text[-4:-1])
print(text[::-1])

text = "hello"
print(text)
# Reassign
text = "hi"
print(text)
# Update value
# text[0] = "H"
print(text)

# string concat
text1= "Hi"
text2= "Hello"
text3 = text1+text2
print(text3)

text1= "Hi"
text2= 10
# string concat cannot be done with other data types
# text3 = text1+text2

# string repeatition
text = "Hi"
repeat_hi = text * 10
print(repeat_hi)

# verify if given string is class or not
str_data = "Hello"
print(type(str_data))

# dir() to get list of all tasks that i can do
print(dir(str))

# help() --> documentation tool
# help(str.isnumeric)

# validate_mobile_number = "90o0067890"
validate_mobile_number = "9000067890"
is_num_valid = validate_mobile_number.isnumeric() 
print(is_num_valid)
# simple variable
value = 10 # regular int
values = 10,20,30 # data structure -> tuple

print(type(value))
print(type(values))

# Create Empty List
empty_list = []
print(type(empty_list))
print(empty_list)

# Create List With Numeric Data
list_nums = [10,20,30,40,50]
print(type(list_nums))
print(list_nums)

# Create List With Text Data
list_courses = ["Python","Java","Cloud"]
print(list_courses)

# Create List With Mixed Data
list_mixed = [1,2,3.5,"Python"]
print(list_mixed)

# Access data in lists
list_nums = [10,20,30,40,50]
# Indexing
print(list_nums[0])
print(list_nums[-1])

# Slicing
print(list_nums[:])
print(list_nums[::])
print(list_nums[::2])
print(list_nums[::-1])

# Memory Management
list_nums_1 = [10,20,30,40,50]
list_nums_2 = [10,20,30,40,50]
print(id(list_nums_1)) # 4375154432
print(id(list_nums_2)) # 4375175104

print(id(list_nums_1[0])) # 4374178384
print(id(list_nums_2[0])) # 4374178384
value = 10
print(id(value)) # 4374178384

# Accessing Out Of Range Elements
list_nums = [10,20,30,40,50]
# print(list_nums[10]) # IndexError: list index out of range

# Loop Through List for accessing/operating on indiviudal elements
# for loop
for i in list_nums:
    print(i) # deafult is new line

# for i in list_nums:
#     print(i,end=" ") 

# for i in list_nums:
#     print(i,end="-") 

# create list with class
list_nums = list()
print(list_nums)   

list_nums = list([10,20,30,40,50])
print(list_nums)

# if we pass an non-iterable object
# list_nums = list(10) # TypeError: 'int' object is not iterable
list_nums = list([10]) 
print(list_nums)

# iterable check 
value = 10 # no __iter__ means not iterable
# print(dir(value))

list_value = [10]
print(dir(list_value)) # we get __iter__ means it's iterable

string_value = "Ravi"
print(dir(string_value)) # we get __iter__ means it's iterable

# Range -> gives range of values
range_values = range(6)
for i in range_values:
    print(i)

range_values_list = list(range(0,51,5))
print(range_values_list)

# perform some operations on list items
# arithmetic operations
for i in range_values_list:
    print(i*2)

# in to check if item is available
days = ["sun","mon","tue","wed","thu","fri","sat"]    
print("wed" in days)
check_day = input("Enter Day Name In a Week: ")
if check_day in days:
    print(f"Day {check_day} Exists")
else:
    print(f"Day {check_day} Doesn't Exist")

print(dir(list_value))
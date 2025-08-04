# Create Empty Tuple
empty_tuples = ()
print(type(empty_tuples))
print(empty_tuples)

# Tuples of numbers
tuple_nums = (10,20,30,40,50)
print(tuple_nums)

# Tuples of strings
tuple_text = ("ravi","krishna","data")
print(tuple_text)

# Tuples of mixed data 
tuple_mixed = ("ravi",2,3.5)
print(tuple_mixed)

# Using tuple class
tuple_new = tuple((10,20,30,40,50))
print(tuple_new)

empty_tuples = tuple()
print(empty_tuples)

# one_tuple = tuple(10) # TypeError: 'int' object is not iterable
# print(one_tuple) 

# list_nums = list([10]) 
# print(list_nums)

# one_tuple = tuple((10)) # TypeError: 'int' object is not iterable
one_tuple = tuple((10,))
print(one_tuple)

# Create tuple using list 
list_nums = [10,20,30,40,50]
tuple_nums = tuple(list_nums)
print(tuple_nums)

# create tuple using range
tuple_new = tuple(range(0,26,5))
print(tuple_new)

# create list using tuples
list_nums = list(tuple_nums)
print(list_nums)

# Accessing same as strings and lists
# indexing starts position at 0, positive & negative indexing
# slicing is also same as strings and lists

tuple_nums = (10,20,30,40,50)
print(tuple_nums[0])

print(tuple_nums[3])
print(list_nums[-1])

# out of range indexing error
# print(tuple_nums[10]) # IndexError: tuple index out of range

# slicing
print(tuple_nums[:])
print(tuple_nums[::])
print(tuple_nums[::2])
print(tuple_nums[::-1])

# Tuples are immutables
list_nums = [10,20,30,40,50]
tuple_nums = (10,20,30,40,50)

list_nums[0] = 100
print(list_nums)

# tuple_nums[0] = 100 # TypeError: 'tuple' object does not support item assignment
print(tuple_nums)

# Loop Through Tuples for accessing/operating on individual elements
# for loop
tuple_nums = (10,20,30,40,50)
for i in tuple_nums:
    print(i) # default is new line

for i in tuple_nums:
    print(i,end=" ") 

for i in tuple_nums:
    print(i,end="-")     
    
tuple_nums = (10,20,30,40,50)
print(dir(tuple_nums))

# Use tuples only for data safety(fixed data/constants)
location_info = {(17.8900, 78.7989): "Hitech City"}
# empty sets
empty_set = {} # always a dict
print(type(empty_set))

# using class
empty_set = set()
print(type(empty_set))

list_nums = [10,20,30,40,50,10,20]
tuple_nums = (10,20,30,40,50,10,20)

print(list_nums)
print(tuple_nums)

print(list_nums[0])
print(tuple_nums[0])


# numbers set
set_nums = {10,20,30,40,50,10,20}
print(set_nums) # Unordered, Unique
# print(set_nums[0]) # Unindex, TypeError: 'set' object is not subscriptable

# subscriptable or not
obj1 = [1,2,3]
print(hasattr(obj1,'__getitem__')) # True -> subscriptable
obj2 = {1,2,3}
print(hasattr(obj2,'__getitem__')) # False -> not subscriptable

# access -> loops
set_nums = {10,20,30,40,50,10,20}
print(dir(set_nums))

for i in set_nums:
    print(i)
    
# Set Operations 

# add() -> adds single element to set
set_nums = {10,20,30,40,50,10,20}
print(set_nums)
set_nums.add(60)
print(set_nums)

set_nums.add(50)
print(set_nums)

# set_nums.add() # TypeError: set.add() takes exactly one argument (0 given)
# set_nums.add(70,80) # TypeError: set.add() takes exactly one argument (2 given)
set_nums.add((70,80))
print(set_nums)


# update() -> adds multiple elements(only iterables)
    # this will update the set in place, meaning original set is updated
set_nums = {10,20,30,40,50,10,20}
print(set_nums)
set_nums.update([70,80])
print(set_nums)

set_nums.update({90,100})
print(set_nums)

# remove() -> removes a specific element, raises error if element 
# not found
set_nums = {10,20,30,40,50,10,20}
print(set_nums)
# set_nums.remove(100) # KeyError: 100
print(set_nums)

# discard() -> removes a specific element, if element is not found
# no error
set_nums = {10,20,30,40,50,10,20}
print(set_nums)
set_nums.discard(100) # No KeyError: 100
print(set_nums)

# pop() -> removes random element and returns the element removed
set_nums = {10,20,30,40,50,10,20}
print(set_nums)
removed_element = set_nums.pop()
print(removed_element)
set_nums.add(removed_element)
print(set_nums)

# clear() -> removes all elements, set will be empty
set_nums = {10,20,30,40,50,10,20}
print(set_nums)
set_nums.clear()
print(set_nums)

# union() -> returns a new sets, with all the unique elements
# from both the sets, you can also use symbol | 
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
s3 = s1.union(s2)
print(s1.union(s2))
print(s3)

s4 = s1 | s2
print(s4)

# intersection() -> returns a new sets, with all the common elements
# from both the sets, you can also use symbol & 
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
s3 = s1.intersection(s2)
print(s1.intersection(s2))
print(s3)


s4 = s1 & s2
print(s4)
print(s1)
print(s2)

# intersection_update() -> updates the calling set to keep only the items
    # found in both sets(common) 
    # modifies the original set -> doesn't return a set again
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.intersection_update(s2))
print(s1)
print(s2)

# difference() -> returns a new set with elements consisting 
# only the elements in first set not the second
# you can also use symbol -
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.difference(s2))
print(s1)
print(s2)

print(s2.difference(s1))

print(s1-s2)
print(s2-s1)

# difference_update() -> update the original set calling, returns nothing
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.difference_update(s2))
print(s1)
print(s2)

s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s2.difference_update(s1))
print(s1)
print(s2)

# symmetric_difference() -> returns a set, with elements that are 
# either of the sets, but not both (exclude common elements)
# you can also use symbol ^
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.symmetric_difference(s2))
print(s1 ^ s2)
print(s1)
print(s2)

# symmetric_difference_update() -> update the original set calling, 
#  with elements that are either of the sets, but not both 
# (exclude common elements)
s1 = {10,20,30,40,50}
s2 = {40,50,60,70,80}
print(s1.symmetric_difference_update(s2))
print(s1)
print(s2)

# issubset() -> checks whether all elements of one set are present
# in another set
s1 = {10,20,30,40,50}
s2 = {30,40,50}
s3 = {30,40,50,60}
print(s2.issubset(s1)) 
print(s3.issubset(s1)) 

# issuperset() -> checks whether a set contains 
# all the elements of another set
s1 = {10,20,30,40,50}
s2 = {30,40,50}
print(s1.issuperset(s2))
print(s2.issuperset(s1))

# isdisjoint() -> checks if two sets have no common elements
s1 = {10,20,30,40,50}
s2 = {30,40,50}
s3 = {60,70,80}
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))

# Frozenset
s1 = {10,20,30,40,50}
s1.add(60)
print(s1)
fs1 = frozenset({10,20,30,40,50})
print(type(fs1))
# fs1.add(60) 
print(dir(fs1))
print(fs1)
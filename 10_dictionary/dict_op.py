# Add or Update Elements
fruits = {"a":"apple","b":"banana"}
print(fruits)
# add an item -> we add with key, no index
fruits["c"] = "cherry"
print(fruits)

# update an item
fruits["a"] = "apricot"
print(fruits)

# delete an item -> we need dict methods

# using dict class
empty_dict = dict()
print(empty_dict)
print(type(empty_dict))

# person dict
person_dict = dict(name="Ravi",age=30,city="hyd")
print(person_dict)

print(fruits)

# loop through dict --> only keys can be retrieved 
for i in fruits:
    print(i)
    
# value can be retrieved through methods     

# Dict methods
# print(dir(fruits))

fruits = {"a":"apple","b":"banana"}
print(fruits)
# add / update items

# update() -> add/update single or multiple items
fruits.update({"c":"cherry"})
print(fruits)
fruits.update({"a":"apricot"})
print(fruits)

fruits.update({"a":"apple","d":"dragon fruit"})
print(fruits)

# pop() -> removes the item with given key
# fruits.pop() # TypeError: pop expected at least 1 argument, got 0
fruits.pop("b")
print(fruits)

# fruits.pop("f") # KeyError: 'f'
print(fruits)

# popitem() -> removes the last inserted item 
fruits.popitem()
print(fruits)

# fruits.popitem("a") # TypeError: dict.popitem() takes no arguments (1 given)
print(fruits)

# clear() -> removes all items from the dictionary
fruits.clear()
print(fruits)

# Access we used [key] 
dict_nums = {1:100, 2:200, 3:300, 4:400}
dict_courses = {"course1":"python","course2":"java","course3":"cloud"}
print(dict_nums[1])
print(dict_courses["course2"])
# print(dict_courses["course4"]) # KeyError: 'course4'

# get() -> Access the value using key, if key not found no error
print(dict_nums.get(1))
print(dict_courses.get("course2"))
print(dict_courses.get("course4","Upcoming Course"))

# keys() -> Gives all the keys
dict_courses = {"course1":"python","course2":"java","course3":"cloud"}
print(dict_courses.keys())

# get keys individually
keys_courses = dict_courses.keys()
for i in keys_courses:
    print(i, end=" ")

# values() -> Gives all the values
dict_courses = {"course1":"python","course2":"java","course3":"cloud"}
print(dict_courses.values())

# get values individually
values_courses = dict_courses.values()
for i in values_courses:
    print(i, end=" ")

# print(values_courses[0]) # TypeError: 'dict_values' object is not subscriptable 
# not subscriptable --> doesn't support indexing

# items() -> get both the keys and values
dict_courses = {"course1":"python","course2":"java","course3":"cloud"}
print(dict_courses.items())

# [('course1', 'python'), ('course2', 'java'), ('course3', 'cloud')] -> list of tuples
keys_values_courses = dict_courses.items()
for i in keys_values_courses:
    print(i, end=" ")

for key in dict_courses.keys():
    print(key,end=" ")

for value in dict_courses.values():
    print(value,end=" ")
print()    

# copy() - creates a shallow copy
dict_courses = {"course1":"python","course2":"java","course3":"cloud"}

dict_courses_copy = dict_courses.copy()
print(dict_courses_copy)

dict_courses_copy["course3"] = "devops"
print(dict_courses_copy)
print(dict_courses)

# soft copy using =
dict_courses = {"course1":"python","course2":"java","course3":"cloud"}
dict_courses_copy_soft = dict_courses
dict_courses_copy_soft["course3"] = "devops"
print(dict_courses_copy_soft)
print(dict_courses)

# setdefault() -> give value of a key, sets if not present
dict_courses = {"course1":"python","course2":"java","course3":"cloud"}
print(dict_courses)
dict_courses.setdefault("course2","devops") # keys exists, so not updated
value = dict_courses.setdefault("course2","devops")
print(value)
print(dict_courses)

dict_courses = {"course1":"python","course2":"java","course3":"cloud"}
print(dict_courses)
dict_courses.setdefault("course4","devops") # keys doesn't exists, so updated
value = dict_courses.setdefault("course4","devops")
print(value)
print(dict_courses)
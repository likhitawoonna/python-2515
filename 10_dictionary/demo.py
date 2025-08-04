# Dictionaries
empty_dict = {}
print(type(empty_dict))

# Store elements using key value pairs
dict_nums = {1:100,2:200,3:300}
print(type(dict_nums))
print(dict_nums)

dict_courses = {"course1":"python","course2":"java","course3":"cloud"}
print(dict_courses)

dict_mixed = {1:"python","two":2,"course":"cloud"}
print(dict_mixed)

# Keys must be Immutables Only(Strings, Numbers, Tuples)
# sample_data = {[10,20]:"ten"} # TypeError: unhashable type: 'list'
sample_data = {(10,20):"ten"}
print(sample_data) 

# Access data --> generally we use methods
dict_courses = {"course1":"python","course2":"java","course3":"cloud"}
print(dict_courses["course1"])
print(dict_mixed[1])
print(dict_nums[2])
# print(dict_nums[5])

print(dir(dict_courses))

# dict inside dict
# Example of a nested dictionary
student_data = {
    "student1": {
        "name": "Alice",
        "age": 18,
        "courses": ["Math", "Physics"]
    },
    "student2": {
        "name": "Bob",
        "age": 19,
        "courses": ["Chemistry", "Biology"]
    }
}
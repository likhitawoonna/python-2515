# methods of tuples
list_nums = [10, 20, 30, 20, 40, 20, 10, 20, 10, 20, 10]
tuple_nums = tuple(list_nums)
print(type(tuple_nums))
print(tuple_nums)
print(tuple_nums.index(40))

print(tuple_nums.index(20,4,8))

tuple_nums = [10, 20, 30, 20, 40, 20, 10, 20, 10, 20, 10]
print(tuple_nums.count(10))

# Tuples have packing and unpacking mechanism
student = "Ravi",25,"Python" # Packing
print(type(student))
stu_name,stu_age,stu_course = student # Unpacking 
# student = "Ravi",25,"Python",25000
# ValueError: too many values to unpack (expected 3) -> LHS = RHS
print(stu_name)
print(stu_age)
print(stu_course)

# list inside tuples
sample_data = ([[10],20],[30,40],[50,60])

sample_data[0][0] = 100
print(sample_data)

# sample_data[1] = [300,400] TypeError: 'tuple' object does not support item assignment
print(sample_data)

# tuples inside list
sample_data = [(10,20),(30,40),(50,60)]
# sample_data[0][0] = 100 # TypeError: 'tuple' object does not support item assignment
sample_data[1] = (300,400)
print(sample_data)
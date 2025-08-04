# List Methods 
list_nums = [10,20,30,40,50]
print(list_nums) # Before append
list_nums.append(60) # one element
print(list_nums) # After append

# list_nums.append(70,80) # multiple element
# TypeError: list.append() takes exactly one argument (2 given)
list_nums.append([70,80])
print(list_nums) # After append --> added as nested list

list_nums.append("Hello")
print(list_nums)

# In Lists we can have duplicates
list_nums.append(60)
list_nums.append("Hello")
print(list_nums)

list_nums = [10,20,30,40,50]
# list_nums.extend(60) --> TypeError: 'int' object is not iterable
list_nums.extend([60]) 
print(list_nums)

list_nums.extend([70,80])
print(list_nums) # After extend --> added as Individually
list_nums.extend("Hello")
print(list_nums)

# list_nums.extend([70,80],[90,100]) --> TypeError: list.extend() takes exactly one argument (2 given)
print(list_nums)

list_nums = [10,30,40,50]
print(list_nums)
list_nums.insert(1,20)
print(list_nums)

list_nums.insert(10,20)
print(list_nums)

list_nums.insert(0,5)
print(list_nums)

list_nums[0] = 15
print(list_nums)

list_nums = [10,20, 30,40,50]
print(list_nums)
list_nums.pop()
print(list_nums)

list_nums = [10,20, 30,40,50]
print(list_nums)
list_nums.pop(2)
print(list_nums)

list_nums = [10,20, 30,40,50]
print(list_nums)
# list_nums.pop(10) --> IndexError: pop index out of range
print(list_nums)

list_nums = [10,20, 30,40,50]
print(list_nums)
list_nums.remove(20)
print(list_nums)
# list_nums.remove(60) --> ValueError: list.remove(x): x not in list
print(list_nums)

list_nums = [10,20, 30,40,50]
print(list_nums)
list_nums.clear()
print(list_nums)

list_nums = [10, 20, 30, 20, 40, 20, 10, 20, 10, 20, 10]
print(list_nums)
print(list_nums.index(40))

print(list_nums.index(20,4,8))

list_nums = [10, 20, 30, 20, 40, 20, 10, 20, 10, 20, 10]
print(list_nums.count(50))

list_nums = [10,20, 30,40,50]
print(list_nums)

backup_list_nums = list_nums.copy() # shallow copy
print(backup_list_nums)

backup_list_nums.append(60)

print("Original: ", list_nums)
print("Updated: ", backup_list_nums)

# Soft copy 
list_nums = [10,20, 30,40,50]
print(list_nums)

backup_list_nums_soft = list_nums # Soft copy
backup_list_nums_soft.append(60)

print("Original: ", list_nums)
print("Updated: ", backup_list_nums_soft)

list_nums = [10,20, 30,40,50]
print(list_nums)

print(list_nums.reverse())
print(list_nums)

list_nums = [10,20, 30,40,50]
print(list_nums)
# print(text[::-1])
print(list_nums[::-1])
print(list_nums)

list_nums = [10,30,20,50,40]
print(list_nums)
print(list_nums.sort(reverse=False)) # ascending
print(list_nums)

print(list_nums.sort(reverse=True)) # descending
print(list_nums)

list_text = ["hi","abc","zoro"]
print(list_text)
print(list_text.sort())
print(list_text)

mixed_list = ["hi",2,3.5,"abc","zoro"]
print(mixed_list)
print(mixed_list.sort())
print(mixed_list)
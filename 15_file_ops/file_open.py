# 1st way
file = open("file.txt","r")
print(file)
print(file.closed)
# manually close
file.close()
print(file.closed)

# 2nd way
with open("file.txt","r") as file_data:
    print(file_data) 
print(file_data.closed)
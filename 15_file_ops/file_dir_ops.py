# Create File
with open("new.txt","w") as file_data:
    print(file_data)
    
# Delete File
import os
os.remove("new.txt")

# Create Folder
os.mkdir("my_folder")

# Delete Folder
os.rmdir("my_folder")
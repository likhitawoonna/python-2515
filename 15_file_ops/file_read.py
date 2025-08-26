with open("file.txt","r") as file_data:
    # print(file_data.read()) # read whole file 
    
    # for i in file_data.read(): # character by character
    #     print(i)
    
    # print(file_data.readline()) # read one line
    # print(file_data.readline()) # read one line
    
    # print(file_data.readlines()) # reads all lines with list and give /n
    data = file_data.readlines()
    for lines in data:
        print(lines.strip())
    
    
    
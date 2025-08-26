# reading csv data 
import csv
with open("sample_data.csv","r") as file_data:
    csv_reader = csv.DictReader(file_data)
    for row in csv_reader:
        # implement same @gmail like functionality earlier we used
        # if row['email'].endswith("@gmail.com"):
        #     print(row)
        
        # find customer mobile or id
        if row["mobile"] == "66090900":
            print(row)
        
        # print(row)
    # print(csv_reader)
    # csv_reader = csv.reader(file_data)
    # print(csv_reader)
    # for row in csv_reader:
        # requirement to fetch all the customers data of hyderabad location
        # using conditional check
        # if row[3] == "hyderabad":
        #     print(row)
            
        # requirement to fetch all the customers who has gmail account
        # if row[1].endswith("@gmail.com"):
        #     print(row)
        
        # working with DictReader
                

    
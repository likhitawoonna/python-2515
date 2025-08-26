# Work with JSON data 
import json

student = {
   "id": 101,
   "name": "Ravi",
   "course": "Python Full Stack",
   "skills": ["Python", "Git", "AWS"],
   "score": 89.5
}

print(type(student))

# writing python data to json file
with open("student.json","w") as file:
    json.dump(student,file,indent=4)

# reading json file and keeping in python data format
with open("student.json","r") as file:
    py_data = json.load(file)
print(type(py_data))
print(py_data)
print("Welcome: ",py_data["name"])

# Directly using data instead of files -> write
student_json = json.dumps(student,indent=4)
print(type(student_json))
print(student_json)

# Directly using data instead of files -> read
student_json_data = json.loads(student_json)
print(type(student_json_data))

# working with web app simulation
with open("users.json","r") as file:
    data = json.load(file)
    filtered_data = []
    for user in data['users']:
        if user['age'] < 30:
            filtered_data.append(user['username'])
print(filtered_data)

with open("filtered_users.json","w") as file:
    json.dump(filtered_data,file,indent=4)
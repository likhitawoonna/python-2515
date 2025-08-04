# Implement Student Management System (LMS) 

# We want System Info(FIXED) To be Stored In Tuples
SYSTEM_INFO = ("LMS Students Portal","v1.0","Edify University")
ADMIN_INFO = ("admin@edify.ai","+91-9876543210","201")

# Display System Info
print("="*50)
print(f"Welcome To {SYSTEM_INFO[0]} {SYSTEM_INFO[1]}")
print(f"Developed By {SYSTEM_INFO[2]} students ")
print("="*50)

# Implement functionalities

# Store Students Info
students = {}

# Design Menu System for various operations
while True:
    print("Choose an option: ")
    print("1 - Add Student")
    print("2 - Modify Student")
    print("3 - Delete Student")
    print("4 - List All Students")
    print("5 - Exit App")
    
    choice = input("Enter Your Choice (1-5): ")
    if choice == "1":
        print("Performing Choice 1 Operation")
        student_id = input("Enter Student ID: ")
        if student_id in students:
            print("Student Already Exists")
        else:
            name = input("Enter Student Name: ").strip().title()
            # Prepare to store multiple scores (can be duplicates)
            scores = []
            while True:
                score_input = input("Enter a score or type done")
                if score_input == "done":
                    break
                if score_input.isdigit():
                    score = int(score_input)
                    if 0 <= score <= 100:
                        scores.append(score)
                    else:
                        print("Invalid Score, only 0-100")
                else:
                    print("Invalid Score, only numbers accepted")
                    
            # Prepare to store multiple skills (cannot be duplicates)
            skills = set()
            while True:
                skill_input = input("Enter a skill or type done")
                if skill_input == "done":
                    break
                skills.add(skill_input.strip().title)
                
                
            # Save the student details so far we collected
            students[student_id] = {
                "name": name,
                "scores": scores,
                "skills": skills
            }
            print("Student Added Successfully")
            print(students)         
        
    elif choice == "2":
       print("Performing Choice 2 Operation")
       student_id = input("Enter Student ID To Modify: ") 
       if student_id in students:
           new_name = input("Enter New Name: ").strip().title()
           students[student_id]["name"] = new_name
           print("Student Updated Successfully")
           print(students)
       else:
           print("Student ID Not Found")
       
    elif choice == "3":
       print("Performing Choice 3 Operation")
    elif choice == "4":
       print("Performing Choice 4 Operation")     
    elif choice == "5":
       print("Performing Choice 5 Operation")
       break
    else:
       print("Invalid Choice select only (1-5)")  
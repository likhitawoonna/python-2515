student_id_valid = False
while not student_id_valid:
    student_id = input("Enter Your ID: ")
    if student_id.isdigit():
        student_id = int(student_id)
        if student_id > 0:
            student_id_valid = True
        else:
            print("Please Enter Positive Number or Above Zero")
    else:
        print("Please Enter Numbers Only, Other characters not allowed")
student_name_valid=False
while not student_name_valid:
    student_name=input("enter student name:")
    student_name=student_name.strip().title()
    check_name=student_name.replace(" ","")
    if check_name.isalpha and len(student_name)>=3:
              student_name_valid = True
              print("Welcome, "+student_name)
    else:
        if not check_name.isalpha():
            print("Name should contain only letters and spaces")
        elif len(student_name) < 3:
            print("Name should contain atleast 3 characters")
stu_attendance=False
while not stu_attendance:
     stu_attendance=input("enter attendance:")
     if stu_attendance.isdigit():
        stu_attendance=int(stu_attendance)
        if stu_attendance > 0 and stu_attendance < 100:
               stu_attendance=True
        else:
               print("the attendance should between 0 to 100")
     else:
        print("attendance should be numbers only")

total_score = 0
no_of_subj = 0

while True:
        subj_score = int(input(f"Enter score for subject {no_of_subj + 1}: "))
        if 0 < subj_score < 100:
             total_score += subj_score
             no_of_subj += 1
             contin = input("Do you want to enter another score? (yes/no): ")
             if contin.lower() != "yes":
                      break
        else:
           print("Score must be greater than 0 and less than 100. Please try again.")
avg_score = total_score/no_of_subj
print("Average score:", avg_score)
if avg_score>85:
    print("excellent")
elif avg_score>=70 and avg_score<=84:
    print("good")
elif avg_score>=50 and avg_score<=69:
    print("average")
else:
    print("needs improvement")

if stu_attendance<=75:
     print("warning low attendance")
else:
     print("attendance satisfied")
     
print(f"enter student id {student_id}")
print(f"enter name of student {student_name}")
print(f"total_score is {total_score}")
print(f"average score is {avg_score}")
print(f"student attendance: {stu_attendance}")
    

    



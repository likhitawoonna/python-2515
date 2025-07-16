student_id=input("enter student id: ")
student_name=input("enter student name: ")
stu_attendance=int(input("enter attendance: "))
total_score = 0
no_of_subj = 0

while True:
    subj_score = int(input(f"Enter score for subject {no_of_subj + 1}: "))
    total_score += subj_score
    no_of_subj += 1

    contin = input("Do you want to enter another score? (yes/no): ")
    if contin.lower() != "yes":
        break

avg_score = total_score/no_of_subj
#print("average score is {avg_score}")

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
print("--------------------display details---------------------------------")
print(f"enter student id {student_id}")
print(f"enter name of student {student_name}")
print(f"total_score is {total_score}")
print(f"average score is {avg_score}")
print(f"student attendance: {stu_attendance}")
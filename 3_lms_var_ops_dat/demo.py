# Concepts Covered - Variables, Data Types, Operators

# Student Details
student_id = 101
student_name = "Ravi"
student_age = 20

# Scores Details
quiz_score = 80
assignment_score = 95
exam_score = 90

# Attendance Details
student_attendance = 95

# Use arithmetic operators to calculate
total_score = quiz_score + assignment_score + exam_score # addition operator
average_score = total_score / 3 # division operator

# Use relational operators to determine
# If the student is passing based on average score 75
is_passed = average_score >= 75 # False

# Use increment operator to update
# Attendance (simulate an additional attended session)
student_attendance = student_attendance + 1 # Correct -> Long Syntax
student_attendance += 1 # Correct -> Concise Syntax (Compound Assignment Operators)


# Use logical operators to determine award eligibility
# If the student qualifies for an award 
# (requires high attendance i.e 90 and above and a passing grade)
qualified_award = student_attendance >= 90 and is_passed

# Student Information Section: ID, Name, Age
# Academic Performance Section: Individual scores, total, and average
# Status Section: Passing status and award eligibility

print("======================")
print(f"Student ID: {student_id}")
print(f"Student Name: {student_name}")
print(f"Student Age: {student_age}")
print(f"Total Score: {total_score}")
print(f"Average Score: {average_score}")

print("===== STUDENT ATTENDANCE REPORT=====")
print(f"Current Attendance: {student_attendance}")

print("======================")
print("===== STUDENT SCORE REPORT=====")
print(f"Student PASSED: {is_passed}")
print(f"Student QUALIFIED FOR AWARD: {qualified_award}")
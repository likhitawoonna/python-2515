# # Concepts Covered - Variables, Data Types, Operators, Type Conversion, Conditionals
print("=========== LMS FEE DISCOUNT CAL==========")

# get user input
student_name = input("Enter Name: ")
student_grade = int(input("Enter Grade(1-12)"))
tuition_fee = float(input("Enter Tuition Fee"))

is_academic_topper_input = input("Academic Topper ? (yes/no) ")
is_academic_topper = is_academic_topper_input == "yes"

# initial discount set
discount = 0.0

# input validation
if 1 <= student_grade <=12:
    # process discount for cal
    print(f"Processing discount for {student_name}")

    # primary discount for 9-12
    if student_grade >=9 and student_grade <=12:
        if is_academic_topper:
            discount = 0.20
            print("Academic Topper Discount Applied")
        else:
           discount = 0.10
           print("Primary School Discount Applied")

    elif student_grade >=6 and student_grade <=8:
        discount = 0.05
        print("Middle School Discount Applied") 
    
    else:
        discount = 0.0
        print("No Discount Applicable for this grades") 

    # match - case
    match student_grade:
        case 10:
            discount += 0.03
        case 12:
            discount += 0.05
        case _:   
            discount += 0.0
    
    discount_amount = tuition_fee * discount
    discounted_fee = tuition_fee - discount_amount

    print("===== LMS Fee Discount Calculator =====")
    print(f"Processing discount for {student_name}")
    print(f"Student Name {student_name}")
    print(f"Student Grade {student_grade}")
    print(f"Academic topper status {is_academic_topper}")
    print(f"Base tuition fee {tuition_fee}")
    print(f"Discount amount saved {discount_amount}")
    print(f"Final tuition fee {discounted_fee}")
    

else:
    print(f"Invalid Grade!, Please enter in between 1-12")
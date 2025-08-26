# class
class Laptop:
    # data -> attributes / variables 
    brand = "Apple"
    screen = 13
    
    # method
    def play_video():
        print(f"Playing Video In 4k Content")

# object
mac = Laptop()


# Student
# class Student:
#     # attributes 
#     student_name = "ravi"
#     student_email = "ravi@gmail.com"
    
#     # __init__ constructor
#     def __init__(self,student_name,student_email):
#         return None
#         return student_email
    
#     # method - defined inside the class
#     # def info(self):
#     #     # print(self.student_name,self.student_email)
#     #     print(Student.student_name,Student.student_email) # accessing with class name
#         # print(student_name,student_email) # NameError: name 'student_name' is not defined
        
# student_ravi_obj = Student("ravi","ravi@gmail.com")
# student_krishna_obj = Student("krishna","krishna@gmail.com")
# print(student_obj)
# print(student_obj.student_name)
# print(student_obj.student_email)
# student_obj.info() # TypeError: info() takes 0 positional arguments but 1 was given
# Student.info() # TypeError: info() missing 1 required positional argument: 'self'

    
# # define a function
# def student_info():
#     student_name = "krishna"
#     student_email = "krishna@gmail.com"
#     print(student_name,student_email)

# # call func
# student_info()

class Student:
    
    # Class Variable common data for all objects of student class
    institute_name = "Edify"
    
    # using constructor
    def __init__(self,student_name,student_email):
        self.student_name = student_name
        self.student_email = student_email
    
    # your methods
    def info(self):
        print("Student Institute: ",Student.institute_name) # preferred for class variables
        # print("Student Institute: ",self.institute_name) - not preferred for class variables
        print("Student Name: ",self.student_name)
        print("Student Email: ",self.student_email)
        
# Data With Multiple Objects
student_one = Student("one","one@gmail.com") 
student_two = Student("two","two@gmail.com") 
student_three = Student("three","three@gmail.com") 

# Call your functionalities / methods
student_one.info()
student_two.info()
student_three.info()
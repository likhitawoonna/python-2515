import random
# Assume the correct OTP is already stored in a variable
otp = random.randint(1000,9999)
print(otp)

# while loop
# After 3 incorrect attempts, display
# Maximum attempts done, try after 24 Hours
count = 3

while count>0:

    # condition
    # If the OTP entered is not 4 digits, display
    # OTP Must be 4 digit number only
    user_otp = int(input("Enter OTP: "))

    if len(str(user_otp))!=4:
        print("OTP Must be 4 digit number only")
    # If the OTP is correct, display:
    # Correct OTP - Success
    if otp == user_otp:
        print("Correct OTP")
        break
    count = count - 1
    
    # last msg to display
else:
    print("max attempt done, try after 24 Hours")
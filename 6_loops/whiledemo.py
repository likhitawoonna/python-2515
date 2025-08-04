# while demo
count = 1
while count <=5:
    print("Count", count)
    count += 1

# If you don't know number of Iterations before hand, use while loop
# password validation
password = "secret"
user_password = ""

while user_password != password:
    user_password = input("Enter Password: ")
print("Access Granted")

# Drink Water Till Bottle is Empty
water_in_bottle = 10
print("Drinking Water")

while water_in_bottle > 0:
    print("Took A Sip, Remaining Sip:", water_in_bottle-1)
    water_in_bottle -= 1
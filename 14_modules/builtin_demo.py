# random
# datetime
# sys -> devops 
# os -> devops
# csv -> data analytics
# json -> full stack 

# Random Module
import random

print(random.random())

print(random.randint(1,10))

# Simulate OTP functionality
print(random.randrange(100000)) 

# Simulate Lottery App
list_lottery = ["LOT1","LOT2","LOT3","LOT4","LOT5"]
print(random.choice(list_lottery))

# Simulate Random Pickup 
list_users = ["us1","us2","us3","us4","us5","us6","us7","us8","us9","us10"]
print(random.choices(list_users,k=3))
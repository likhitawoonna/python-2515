# break - terminate loop, even if the condition hasn't finished
for i in range(10):
    if i == 5:
        break # loop will terminate here
    print(i)

# continue - skip the current Iteration
for i in range(10):
    if i == 5:
        continue # skip this iteration
    print(i)

# pass - placeholder that does nothing
if 5<9:
    pass
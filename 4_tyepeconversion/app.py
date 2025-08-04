# Type Conversion

a = 100 # int
b = 3.5 # float
c = a + b # Python will convert to float  automatically
print(c)
print(type(c))

# Type Casting - no data loss
x = 100 # int
y = float(x) # y should be float
print(x)
print(y)
print(type(y))

# Type Casting - data loss
l = 3.14
m = int(l)# l should be int
print(l)
print(m)
print(type(m))

# Above are for numeric types

# Text To Numeric or vice versa
x = "100"
y = int(x)+10
# y = x+10 --> TypeError: can only concatenate str (not "int") to str

print(y)
print(type(y))

z = 10 # int
num_text = str(z)
print(type(num_text))

# non-numeric string

x = "hello"
# y = int(x) --> ValueError: invalid literal for int() with base 10: 'hello'

x = 1j
# y = int(x) --> TypeError: can't convert complex to int
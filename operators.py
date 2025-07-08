'''-> Interpolation

        -> In context of Programming, Interpolation means REPLACING PLACEHOLDERS with 
        ACTUAL VALUES

        -> To achieve this, we can use f-strings(Formatted String Literals) in Python

        -> In f-strings we use { } to Represent variables which will be replaced with ACTUAL values

    -> Operators

        -> Special symbols, that performs operations on variables and values(Operands)

        -> We use Operators to Manipulate variables

        -> Types

            -> Arithmetic Operators 

                -> Mathematical Calculations

                -> + - * / % // **

            -> Compound Assignment Operators

                ->  Combine Assignment operator with Arithmetic Operators  

                -> =,+=, -=, *= etc  

                -> For concise (shorter) syntax

                -> x = x + 5 or -> x += 5

                -> Other Programming Languages like java we have decrement(--) and increment(++) 

                    -> NOTE: python doesn't support decrement(--) and increment(++) 
            
            -> Comparison / Relational Operators

                -> Used to compare values and returns a boolean

                -> ==, !=, >, <, <=, >=  

                -> For strings it will check, Lexicographical order i.e Dictionary Order
                   based on ASCII Values

            -> Logical Operators

                -> Used to combine multiple conditions

                -> and, or, not

                X       Y           X and Y         X or Y    not X

                T       T              T              T         F
                T       F              F              T         F     
                F       T              F              T         T
                F       F              F              F         T

            -> Membership Operators   

                -> Used to check if a sequence is present

                -> If sequence found, returns True
                -> If sequence not found, returns False

                    -> in 
                    -> not in

            -> Identity Operators

                -> Used to compare the Objects, not if they are equal(==)

                    -> is
                    -> is not

            -> Bit Wise Operators

                -> Used to perform operations on binary bits

                -> Use Cases - Embedded Systems, Network Programming etc

                -> &(AND), |(OR), ^(XOR), ~(NOT), <<(Left Shift), >>(Right Shift)

                -> & : sets each bit to 1 if both are 1
                -> | : sets each bit to 1 if of of the bit is 1
                -> ^ : sets each bit to 1 if only one of the bits is 1
                        -> meaning if both values are different then output is 1, 
                            if both values are same then output is zero
                -> ~ : inverts the bits

                -> << : Shift left pushing zeros in from right, let the leftmost bits fall off

                -> >> : Sift right by pushing the leftmost bits from the left, 
                    let the rightmost bits fall off
'''


# Arithmetic Operators 
num1 = 3
num2 = 2
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2) # quotient 
print(num1%num2) # remainder
print(num1//num2) # quotient is round off to nearest integer
print(num1**num2) # expo (square of)

# Compound Assignment Operators
num = 10
# num = num + 5
# num += 5 
# num -= 5
num *= 5
print(num)

# Comparison Operators
num1 = 3
num2 = 2
isEqual = num1 == num2
isnotEqual = num1 != num2
isgreatEqual = num1 >= num2
print(isEqual)
print(isnotEqual)
print(isgreatEqual)

str1 = "Python"
str2 = "Django"
str3 = "Django"
str4 = "PYTHON"
str5 = "PYTHOn"


print(str1 == str2)
print(str2 == str3)

print(str1 > str2)
print(str4 > str5)

# Logical Operators
num1 = 7
num2 = 5
num3 = 3
num4 = 5

# T and T --> T
resultAnd = num1 > num2 and num3 > num4
resultNot = num1 > num2
print (resultAnd) 
print (not resultNot) 

# Membership Operators   
text = "Python in an programming language"
isZpresent = 'Z' in text
islpresent = 'l' in text
ispatternPrestent = 'prog' in text
isJavaPresent = 'java' not in text
print(isZpresent)
print(islpresent)
print(ispatternPrestent)
print(isJavaPresent)

courses_list = ["java","python","cloud","devops"]
inpythonPresent = 'python' in courses_list
print(inpythonPresent)

# Identity Operators   
# immutables
num1 = 10
num2 = 10

list1 = [1,2,3]
list2 = [1,2,3]

print(num1 is num2)
print(num1 == num2)

print(list1 is list2) 
print(list1 == list2)

# Bit Wise Operators
a = 5 # 0000000000000101
b = 3 # 0000000000000011 

result = a & b # 0000000000000001
print(result)

result = a | b # 0000000000000111
print(result)

result = a ^ b # 0000000000000110
print(result)

result = ~b # 1111111111111100
print(result)

print(3<<2) # 0000000000000011 --> 0000000000001100
print(3<<1) # 0000000000000011 --> 0000000000000110
print(3<<4) # 0000000000000011 --> 0000000000110000

print(3>>1) # 0000000000000011 -->  0000000000000001
print(3>>3) # 0000000000000011 -->  0000000000000000
print(8>>2) # 0000000000001000 -->  0000000000000010
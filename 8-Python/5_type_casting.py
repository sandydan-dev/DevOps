# Python Casting

# Specify a variable type
# there are many times when you want to specify a type on to a variable. this can be done with type-casting. Python is a object oriented language, and such it use classes to define data types, including is primitive types.

# casting in python is therefore done using constructor functions:

# int() : contructs an integer number from an integer literal, a float literal (by removing all decimal), or a string literal (providing the string represent a whole number). 

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

# float() : contructs a float number from an integer literal, a float literal or string literal (providing the string represents a float or an integer)

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

# str() : contructs a string from a wide variety fo data types, including strings, integers literal and float literals  

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
# Python Numbers

# there are three types of numbers
# 1 : int
# 2 : float
# 3 : complex

# Variables are numeric types are created when assign a value to them:
x = 1
x = 2.3
x = 1j

#todo: int
# Int, or integer is a whole number, positive or negative without decimal, of unlimited lenght.

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z)) 

#!-----------

#todo: float
# Float, or 'floating point number' positive or negative, containing one or more details. 

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

#!-----------

#todo: Complex
# complex numbers are written with a "j" as the imaginary part. 

x = 3+5j
y = 5j 
z = -5j

print(type(x))
print(type(y))
print(type(z))   

#!-----------

#todo: Type conversion

# you can convert from one type to another type with the 'type()' function, using "int()", "float()" and "complex()"

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#!-----------

#todo: Random Number
# python does not have a random() function to make a random number, but python has a built in module called 'random' that can be used to make random number. 

# Import the random module, and display a random number from 1 to 9

import random

print(random.randrange(1,10))

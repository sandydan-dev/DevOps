# Python Variables

# Variables are containers for storing data values.

# Creating Variables
# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.

# x = 5
# y = "John"
# print(x)
# print(y)

# --------------------------------

# Casting
# If you want to specify the data type of a variable, this can be done with casting.

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# -------------------------------

# Get the Type
# You can get the data type of a variable with the type() function.

x = 5
y = "John"
print(type(x))
print(type(y))

# Single or Double Quotes?
# String variables can be declared either by using single or double quotes:

x = "John"
# is the same as
x = 'John'

# ------------------------------

# Variable Names
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

# Legal variable names:

# myvar = "John"
# my_var = "John"
# _my_var = "John"
# myVar = "John"
# MYVAR = "John"
# myvar2 = "John"

# ------------------------------

# Many Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line:

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
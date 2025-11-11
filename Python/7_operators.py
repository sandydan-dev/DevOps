# Python Operators

# Operators are used to perform operations on variables and values.

# Python divides the operators in the following groups:

# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators


#todo: Python Arithmetic Operators


#   Operator	   Name     	   Example	
#     +	          Addition	        x + y	
#     -	          Subtraction	    x - y	
#     *	         Multiplication	    x * y	
#     /	           Division	        x / y	
#     %	            Modulus	        x % y	
#    **	         Exponentiation     x ** y	
#.   //	         Floor division	    x // y	


x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)



#todo: Python Assignment Operators
# Assignment operators are used to assign values to variables:

#      Operator	         Example	     Same As	
#         =	              x = 5	          x = 5	
#        +=	              x += 3	      x = x + 3	
#        -=	              x -= 3	      x = x - 3	
#        *=	              x *= 3	      x = x * 3	
#        /=	              x /= 3	      x = x / 3	
#        %=	              x %= 3	      x = x % 3	
#.       //=	          x //= 3	      x = x // 3	
#        **=	          x **= 3	      x = x ** 3	
#        &=	              x &= 3	      x = x & 3	
#        |=	              x |= 3	      x = x | 3	
#        ^=	              x ^= 3	      x = x ^ 3	
#        >>=	          x >>= 3	      x = x >> 3	
#        <<=	          x <<= 3	      x = x << 3	
#        :=	              print(x := 3)	  x = 3
#                                         print(x)

# The Walrus Operator
# Python 3.8 introduced the := operator, known as the "walrus operator". It assigns values to variables as part of a larger expression:

numbers = [1, 2, 3, 4, 5]
count = len(numbers)
if count > 3:
    print(f"List has {count} elements")

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")





#todo: Python Comparison Operators

# Comparison Operators
# Comparison operators are used to compare two values:

#     Operator	          Name          	Example	
#       ==	              Equal	             x == y	
#.      !=	              Not equal          x != y	
#       >	              Greater than	     x > y	
#       <	              Less than	         x < y	
#       >=	        Greater than or equal to	x >= y	
#       <=	           Less than or equal to	x <= y



# Comparison operators return True or False based on the comparison:

x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)



#todo: Python Logical Operators
# Logical Operators
# Logical operators are used to combine conditional statements:


# Operator	Description	                                   Example	
# and 	    Returns True if both statements are true	   x < 5 and  x < 10	
# or	    Returns True if one of the statements is true	   x < 5 or x < 4	
# not	    Reverse the result, returns False if the result is true	not(x < 5 and x < 10)	


# Test if a number is greater than 0 and less than 10:

x = 5

print(x > 0 and x < 10)



#todo: Python Identity Operators

# Identity Operators
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:


# Operator	Description	                                             Example	
# is 	    Returns True if both variables are the same object	     x is y	
# is not	Returns True if both variables are not the same object   x is not y

# The is operator returns True if both variables point to the same object:

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)


# Difference Between is and ==
# is - Checks if both variables point to the same object in memory
# == - Checks if the values of both variables are equal
# Example
# x = [1, 2, 3]
# y = [1, 2, 3]

# print(x == y)
# print(x is y)



#todo: Membership Operators

# Membership operators are used to test if a sequence is presented in an object:


# Operator	  Description	                                                                   Example	
# in 	      Returns True if a sequence with the specified value is present in the object	   x in y	
# not in	  Returns True if a sequence with the specified value is not present in the object x not in y


# Check if "banana" is present in a list:

fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)


# Check if "pineapple" is NOT present in a list:

fruits = ["apple", "banana", "cherry"]

print("pineapple" not in fruits)



# Membership in Strings
# The membership operators also work with strings:

text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)



# Left-to-Right Evaluation
# If two operators have the same precedence, the expression is evaluated from left to right.

# Example
# Addition + and subtraction - has the same precedence, and therefore we evaluate the expression from left to right:

print(5 + 4 - 7 + 3)
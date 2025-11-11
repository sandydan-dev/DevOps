'''
Python Comments

Comments can be used to prevent execution when testing code.

Creating a Comment
Comments starts with a #, and Python will ignore them:

'''
#This is a comment
print("1, Hello, World!")

# Comments can be placed at the end of a line, and Python will ignore the rest of the line:
print("2, Hello, World!") #This is a comment


# -------------------------------
#Multiline Comments
# Python does not really have a syntax for multiline comments.
# To add a multiline comment you could insert a # for each line:

#This is a comment
#written in
#more than just one line
print("3, Hello, World!")

"""
Since Python will ignore string literals that are not assigned to a variable, you can add a multiline string (triple quotes) in your code, and place your comment inside it:

"""

"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")
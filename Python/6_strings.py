# Python Strings

# Strings

# Strings in python are surrounded by either single quotation mark or double quotation marks. 

# 'Hello'  is same as "Hello"  ( inside quoation )

print("Hello")
print('Hello')

#todo: quotes inside quotes 
# you can use quotes inside a string, as long as they dont match the quotes surrounding the string:

print("It's alright")
print("He is called 'johny'")
print('She is a "Alice"')


#todo: Assign a string to a variable
# assigning a string to variable is done with the variable name followed by an equal sign (=) and the thing. 

a = "Hello var"
print(a)


#todo: Multiline strings
# you can assign a multiline string to a variable by using three quotes 

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Or three single quotes:

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
print(" ")

#todo: String are Arrays

# Like many other popular programming languages, string in python are arrays of unicode characters. 
# However, python does not have a character data types, a strings character is simply a string with a length of 1. 
# Square brackets, can be used to access elements of the string. 

## Get the characher at position 1 (remember that the first character has the postion 0).

a = "Hello, World!"
print(a[0]) # Result : H


#todo: Looping Through a String
# Since strings are arrays, we can loop through the characters in a string, with a for loop.

# Loop through the letters in the word "banana":

for x in "banana":
  print(x)
  
# String Length
# to get the length or the string using len() function
# The len() function returns the length of a string:

print(len(a))  


#todo: Check String
# to check a certain phase or character is present in the string. so we can use keyword in. 

# check if "free" is present in the string 
txt = "The best things in life are free!"
print("free" in txt)


# Use it in an if statement:

if 'free' in txt:
    print("yes")

# Check if NOT
# to check if a certain phrase or character is NOT in a string, we can use keyword 'not in'...

# Check if "expensive" is NOT present in the following text:

txt = "The best things in life are free!"
print("expensive" not in txt)
#!--------------------------------------------------------------


#todo: Python - Slicing Strings

# Slicing

# you can return a range of character by using the slice syntax
# Specify the start index and the end index, separated by a colon, to return a part of the string.

# Get the characters from position 2 to position 5 (not included):

b = "Hello, World!"
print(b[2:5])


#todo: Python - Format - Strings

# String Format
# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

age = 36
#This will produce an error:
txt = "My name is John, I am " + age
print(txt)


# But we can combine strings and numbers by using f-strings or the format() method!

# F-Strings
# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

# To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

# Example
# Create an f-string:

age = 36
txt = f"My name is John, I am {age}"
print(txt)

















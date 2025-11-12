# Python Data Types

# Built-in Data Types
# Variables can store data of different types, and different types can do different things.

# Text Type          :	str
# Numeric Types      :	int, float, complex
# Sequence Types     :	list, tuple, range
# Mapping Type       :	dict
# Set Types          :	set, frozenset
# Boolean Type       :	bool
# Binary Types       :	bytes, bytearray, memoryview
# None Type          :	NoneType (None)

# -----------------------

# Getting the Data Type
# You can get the data type of any object by using the type() function:

# x = 5
# print(type(x))


#todo: Setting the Data Type
# In Python, the data type is set when you assign a value to a variable:

#todo: str  (string) type
x = "Hello World"

#display x:
print(x)

#display the data type of x:
print(type(x)) 
#! -----------------

#todo: int  (integer) type
x = 20

#display x:
print(x)

#display the data type of x:
print(type(x)) 
#! -----------------

#todo: float type
x = 20.5

#display x:
print(x)

#display the data type of x:
print(type(x))
#! -----------------

#todo: complex type
x = 1j

#display x:
print(x)

#display the data type of x:
print(type(x))
#! -----------------

#todo: list type
x = ["apple", "banana", "cherry"]

#display x:
print(x)

#display the data type of x:
print(type(x)) 
#! -----------------

#todo: tuple type
x = ("apple", "banana", "cherry")

#display x:
print(x)

#display the data type of x:
print(type(x)) 
#! -----------------

#todo: range type
x = range(3, 10)

#display x:
print(x)

#convert to list to display the content of x:
print(list(x))
#! -----------------

#todo: dict type (dictionary) 
x = {"name" : "John", "age" : 36}

#display x:
print(x)

#display the data type of x:
print(type(x)) 
#! -----------------

#todo: set type
x = {"apple", "banana", "cherry"}

#display x:
print(x)

#display the data type of x:
print(type(x)) 
#! -----------------

#todo: frozenset type
x = frozenset({"apple", "banana", "cherry"})

#display x:
print(x)

#display the data type of x:
print(type(x)) 
#! -----------------

#todo: bool type
x = True

#display x:
print(x)

#display the data type of x:
print(type(x)) 
#! -----------------

#todo: bytes type
x = b"Hello"

#display x:
print(x)

#display the data type of x:
print(type(x))
#! -----------------

#todo: bytearray type
x = bytearray(5)

#display x:
print(x)

#display the data type of x:
print(type(x)) 
#! -----------------

#todo: memoryview type
x = memoryview(bytes(5))

#display x:
print(x)

#display the data type of x:
print(type(x)) 
#! -----------------

#todo: NoneType
x = None

#display x:
print(x)

#display the data type of x:
print(type(x)) 
#! -----------------
















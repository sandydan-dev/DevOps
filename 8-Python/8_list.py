# Python Lists

mylist = ["apple", "banana", "cherry"]


#todo: List
# Lists are used to store multiple items in a single variable.

# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

# Lists are created using square brackets:

# Create a List:

thislist = ["apple", "banana", "cherry"]
print(thislist)


# List Items

# list items are ordered, changeable, and allow duplicates values. 
# list items are indexed, the first item has index [0], and second item index has [1] etc... 

# Ordered
# When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

# If you add new items to a list, the new items will be placed at the end of the list.


# Changeable
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.


# Allow Duplicates
# Since lists are indexed, lists can have items with the same value:

# Lists allow duplicate values:

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


# List Length
# to determine how many items a list has, use the 'len()' function. 

# Print the number of items in the list:

thislist = ["apple", "banana", "cherry"]
print(len(thislist))



# List Items - Data Types
# List items can be of any data type:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]


# A list can contain different data types:

list1 = ["abc", 34, True, 40, "male"]



# type() function

# From Python's perspective, lists are defined as objects with the data type 'list':

# <class 'list'>

# What is the data type of a list?

mylist = ["apple", "banana", "cherry"]
print(type(mylist))


# The list() Constructor
# It is also possible to use the list() constructor when creating a new list.

# Using the list() constructor to make a List:

thislist = list(('apple', 'banana', 'kiwi', 'mango')) # note the double round-brackets
print(thislist)




#todo: Python - Access List Items

# Access Items
# list item are indexed and you can access them by referring to the index number

# Print the second item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[1])


# todo: Negative Indexing
# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.

# Print the last item of the list:

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

 
# todo: Range of Indexes
# you can specify a range of indexes by specifying where to start and where to end the range. 
# when specifying a range, the return value will be a new list with specified items. 

# return the third, fourth, and fifth item
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) 



# todo: Change item value
# to change the value of a specific item, refer to index number:

# change the second value
thislist = ["apple", "banana", "cherry"]
print(thislist)
# change item value
thislist[1] = "blackberry"
print(thislist)


#todo: Change a Range of Item Values
# to change the value of items within a a specific range, define a list with the new value, and refer to the range of index numbers where you want to insert new value

# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)



# todo: Insert Items
# to insert a new item, without replacing any existing values, we can use the 'insert()' method. 
# the 'insert()' method insert an item at the specified index:

# Insert "watermelon" as the third item:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelan")
print(thislist) 


# todo: Python - Add List Items
# Append items
# to add an item to the end of the list, use the 'append()' method. 

# using append() method to add item in the end of list
thislist = ["apple", "banana", "cherry"]
# add item in end of list
thislist.append("guava")
print(thislist)


#todo: Extend list 
# to append elements from another list to the current list, use the 'extend()' method. 

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
# add another list to current list
thislist.extend(tropical)
print(thislist)



# todo: Add any iterable
# the 'extend()' method does not have to append lists, you can add any iterable object (tuples, sets, dict, etc)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)



# todo: Python - Remove List Items
# Remove Specified Item

# the 'remove()' method removes the specific item. 
# Remove "banana":

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")  # removing item
print(thislist)

# If there are more than one item with the specified value, the remove() method removes the first occurrence:

# Remove the first occurrence of "banana":

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)


# todo: Remove Specified Index

# The "pop()" method removes the specific index item 
# If you do not specify the index, the pop() method removes the last item.

# Removes the second item:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


# The del keyword also removes the specified index:
# Remove the first item:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# The del keyword can also delete the list completely.

# Delete the entire list:

thislist = ["apple", "banana", "cherry"]
del thislist


# todo: Clear the List

# the "clear()" method empties the list. 
# the list still remains, but it has no content

# Clear the list content:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)



# todo: Python - Loop Lists

# Loop Through a List
# you can loop through the list items by using a "for" loop

# Print all items in the list, one by one:

thislist = ["apple", "banana", "cherry"]

for x in thislist:
    print(x)



# todo: Loop Through the Index Numbers

# you can also loop through the list items by referring to their index number. 
# use the "range()" and "len()" function to create a suitable iterable

# Print all items by referring to their index number:

thislist = ["apple", "banana", "cherry"]

for x in range(len(thislist)):
    print(thislist[x])



# todo: List Comprehension

# list comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list 

# based on the list of fruits, you want a new list, containing only the fruits with the letter 'a' in the name

# without list comprehension you will have to write 'for' statement with a conditional test inside:


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

 
# With list comprehension you can do all that with only one line of code:
# The Syntax
# newlist = [expression for item in iterable if condition == True]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "e" in x]

print(newlist)



















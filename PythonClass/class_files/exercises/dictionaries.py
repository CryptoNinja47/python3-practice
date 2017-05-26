# coding: utf-8

'''
Dictionaries

A dictionary entry contains a key and an associated value.
Dictionaries are treated like lists, but unlike lists they have no order.

Dictionaries are more efficient than lists when you need to look up things. 
The longer a list is, the longer it takes to search through it.
No matter how many entries a dictionary has, it takes the same amount of time to retrieve a value.

Documentation:
	https://docs.python.org/2/tutorial/datastructures.html#dictionaries

'''

# Create an empty dictionary by using curly braces.
appledir = {}

# This sets the key 'Tim' to have the value 'CEO'.
appledir['Tim'] = 'CEO'

# Access a value using the key as the index.
print appledir['Tim']

# Giving the same key a new value replaces the previous value.
appledir['Tim'] = 'Buzz Lightyear'
print appledir['Tim']


# To create a dictionary from scratch:
appledir = {'Tim': 'CEO', 'Angela': 'Retail'}

# If you try to access a key that doesn't exist, it's an error.
# To check for a key before using it:
if 'Bob' in appledir:
	print appledir['Bob']
else:
	print "Unknown"

# The get function does the same as the if/else above:
# It either returns the value, or if the key doesn't exist, it returns whatever you specify.
print appledir.get('Bob', 'Unknown')

# You can iterate through a dictionary using a for loop.
for key in sorted(appledir):
	value = appledir[key]
	print key, ":", value

# The items() function returns a tuple with both the key and value.
for key, value in sorted(appledir.items()):
	print key, ":", value

# By default you can only sort by key, not by the value.
# But we can define a function to sort by the value.
def sort_by_value(key_value_tuple):
	return key_value_tuple[1]

for key, value in sorted(appledir.items(), key = sort_by_value):
	print key, ':', value



# Dictionaries inside of lists.
attributes = [{'color': 'red',  'height': 10},
              {'color': 'blue', 'height': 45},
              {'color': 'pink', 'height': 23}]

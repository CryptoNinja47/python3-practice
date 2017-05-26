# coding: utf-8

'''
Lists

Lists have an order to their items, and are changeable (mutable).

Documentation:
	https://docs.python.org/2/tutorial/introduction.html#lists
'''


# Square brackets create an empty list.
animals = []

# The append() function adds an item to the end of the list.
animals.append('cat')
animals.append('frog')
animals.append('bird')

# To access an item in the list, indicate the item number in brackets.
# Python lists are zero-based, meaning the first item is item #0.
first = animals[0]

# Negative numbers index from the end of the list, so -1 is the last item in the list.
last = animals[-1]

# You can change an item in the list.
animals[1] = 'swallow'




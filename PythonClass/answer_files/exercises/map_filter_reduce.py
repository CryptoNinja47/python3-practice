# coding: utf-8

'''
Map/Filter/Reduce

This is a programming pattern strongly associated with functional programming:

1. Map a large set of data into a normalized form.
2. Filter that data down.
3. Reduce it to a single value that answers a question.

Documentation:
	https://docs.python.org/2.7/tutorial/datastructures.html#functional-programming-tools

In Python, consider using comprehensions as a more "Pythonic" approach to map/filter/reduce.
'''

# The question is: How many Apple stores are in Florida?
import csv
from collections import namedtuple
Store = namedtuple('Store', 'state, city, neighborhood')

# map() applies the specified function to each item in the list and returns a list of the results.
stores = map(Store._make, csv.reader(open('data/us_stores.csv')))

'''
# This is the more verbose way to provide a filter function.
def is_florida(store):
	if store.state == 'Florida':
		return True

florida_stores = filter(is_florida, stores)
'''

'''
lambda functions

Another concept associated with functional programming is anonymous functions created on the spot.
In Python this is called a 'lambda' -- you indicate what arguments are taken, then provide
the operation (the body of the function) right there. This allows you to avoid creating
a heavyweight function and makes it easier for Python to handle the functionality in a highly
efficient manner.
''' 
florida_stores = filter(lambda store: store.state == 'Florida', stores)

total = len(florida_stores)

print "There are {} stores in Florida.".format(total)

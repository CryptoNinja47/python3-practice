# coding: utf-8

'''
Generator

A generator returns one item, then is in a frozen state until the next item is requested.
This allows for iterating through large amounts of data without having to load it all 
into memory at once.

The simple way to create a generator is to use 'yield' instead of a return statement.
yield returns the value and freezes the function at that point.

'''

import csv
from collections import namedtuple
Store = namedtuple('Store', 'state, city, neighborhood')

# TODO: Convert the stores() function to be a generator.
def stores():
	stores = []
	for row in csv.reader(open('data/us_stores.csv')):
		store = Store._make(row)
		stores.append(store)
	return stores

for store in stores():
	print "{}, {} ({})".format(store.city, store.state, store.neighborhood)

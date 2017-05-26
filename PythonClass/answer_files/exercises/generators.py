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


def stores():
	for row in csv.reader(open('data/us_stores.csv')):
		yield Store._make(row)

for store in stores():
	print "{}, {} ({})".format(store.city, store.state, store.neighborhood)


# Generator comprehension -- using parenthesis returns a generator instead of a list.
stores = (Store._make(row) for row in csv.reader(open('data/us_stores.csv')))

for store in stores:
	print store.state


def menu():
	yield "spam"
	yield "eggs"
	yield "swallow"

generator = menu()
print next(generator)

for item in generator:
	print item


# A generator, but one that isn't good because it keeps the list in memory...
def animals():
	animals = ['bird', 'cow', 'sparrow']
	for animal in animals:
		yield animal

for animal in animals():
	print animal




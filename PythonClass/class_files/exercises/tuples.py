# coding: utf-8

'''
Tuples

A tuple is a light-weight list that is immutable.
It's used to quickly pass around related values, and often to represent a row from 
a database or spreadsheet.

Documentation:
	http://www.tutorialspoint.com/python/python_tuples.htm
'''
# Basic tuples
animals = ('frog', 'bird', 'horse')

print animals[1]

# A workaround for changing a tuple is to turn it into a list,
# change it, and turn it back into a tuple.
mylist = list(animals)
mylist[1] = 'cat'

animals = tuple(mylist)
print animals

# You can get a sorted copy of a tuple.
# If you sort a list of tuples, Python starts by sorting on the first value, then the second, etc.
print sorted(animals)


'''
Named tuples

The collections module provides useful alternate versions of collection classes.
The named tuple is particularly convenient when dealing with data from a database
or spreadsheet.
'''
from collections import namedtuple

Store = namedtuple('Store', 'state, city, neighborhood')

store = Store(state    = 'Mississippi',
	          city     = 'Ridgeland',
	          neighborhood = 'Renaissance at Colony Park')

# You can access using the list syntax or by name.
print store[0]
print store.state

# Filling a tuple from a list.
values = ['Arkansas', 'Little Rock', 'The Promenade at Chenal']
store = Store._make(values)
print store

# Create a list of store tuples by reading the 'data/us_stores.csv' file.
import csv
stores = []
for row in csv.reader(open('data/us_stores.csv')):
	store = Store._make(row)
	stores.append(store)

for store in stores:
	print "{}, {} ({})".format(store.city, store.state, store.neighborhood.strip())


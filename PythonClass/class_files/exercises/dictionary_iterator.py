# coding: utf-8

'''
Non-ordered list iterator 

If your object represents an unordered list, like a dictionary, you can implement:

	__iter__()
	next()

This is more complex than a list iterator, because we have to track our own state
so we know which item to return next.
'''

import re
import csv

from collections import namedtuple
Entry = namedtuple('Entry', 'name, team, role, email')



class Directory(object):
	def __init__(self):
		entries = [Entry._make(row) for row in csv.reader(open('../exercises/data/apple_dir.csv'))]
		self.entries = {entry.name: entry for entry in entries}
		self.names = None

	def __iter__(self):
		return self

	def next(self):
		# Is this the first time through the for loop?
		if not self.names:
			self.names = self.entries.keys()
			self.current_index = 0

		# Is this the last time through the for loop?
		# Python knows to stop when we raise a StopIteration exception.
		if self.current_index == len(self.names):
			self.names = None
			raise StopIteration

		# Okay, return the current item and increment current_index for next time.
		name = self.names[self.current_index]
		entry = self.entries[name]
		self.current_index += 1
		return name, entry


apple_dir = Directory()

for name, entry in sorted(apple_dir):
	print name + ":", entry


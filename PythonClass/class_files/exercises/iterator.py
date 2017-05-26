# coding: utf-8

'''
Iterators

Iterators -- objects that let you step through data -- are central to Python.
You can implement special methods in your own classes that will allow you
to make use of the iterator features of the built-in Python classes.

'''

import re

'''
Ordered list iterator

If your object represents an ordered list, you just need to implement these two methods:

	__len__()
	__getitem__()
'''
class Sonnet(object):
	def __init__(self, title, author, filename):
		self.title = title
		self.author = author
		with open(filename, 'r') as myfile:
			self.text = myfile.read()
		self.words = re.findall("[\w+']+", self.text)

	def __str__(self):
		return self.text

	# TODO: Add the __len__() and __getitem__() functions...

sonnet = Sonnet('Sonnet 18', 'Shakespeare', 'data/Sonnet.txt')

# TODO: Use list functionality on the sonnet.
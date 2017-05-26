# coding: utf-8

'''
Iterators

Iterators -- objects that let you step through data -- are central to Python.
You can implement special methods in your own classes that will allow you
to make use of the iterator features of the built-in Python classes.

Documentation:
	https://docs.python.org/2.7/tutorial/classes.html#iterators

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

	def __len__(self):
		return len(self.words)

	def __getitem__(self, position):
		return self.words[position]


sonnet = Sonnet('Sonnet 18', 'Shakespeare', 'data/Sonnet.txt')

print sonnet
print sonnet.words

print len(sonnet)
print sonnet[15]
print sonnet[5:13]

for word in sonnet:
	print word

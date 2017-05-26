# coding: utf-8


''' Useful functions for the Python class. '''

'''
TODO: 
	1. Create a function called words().
	2. The function should take a text argument, and use the string's split() function to return a list of the words found in the text.

The syntax for defining a function is:

	def func_name(argument1, argument2):
		# code
		return result
'''


def words(text):
	''' Returns a list of words from the text. '''
	words = text.split()
	count = len(words)
	return words, count


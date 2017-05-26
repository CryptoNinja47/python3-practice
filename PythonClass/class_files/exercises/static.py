# coding: utf-8

'''
A static method is just like a stand-alone function, but it belongs to a class.
It doesn't take either self or cls as an argument.
It's a way to organize functions in a namespace if you wish.
'''
class TextHandling(object):

	@staticmethod
	def words(text):
		return text.split()


print TextHandling.words("Here's to the crazy ones")
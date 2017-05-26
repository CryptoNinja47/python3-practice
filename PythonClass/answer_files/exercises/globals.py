# coding: utf-8

'''
Functions

'''

# Global vs local variables
monty = 'flying'

def myfunction():
	'''
	You can access a global variable from within a function, 
	but if you change it, Python creates a local copy that "shadows" the global.
	If you want to change the global value, you must specify at the top
	of the function that you are using the global version.
	'''
	global monty
	monty = 'circus'
	print 'In function, monty =', monty

myfunction()
print 'Globally, monty =', monty

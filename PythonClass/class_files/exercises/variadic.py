# coding: utf-8

'''
variadic functions accept an arbitrary number of arguments.
Prefixing an argument name with '*' creates a list of the remaining positional arguments that were passed in.
Prefixing an argument name with '**' creates a dictionary of the named arguments that were passed in.
'''

# x and y here are 'positional arguments'.
def multiply(x, y):
	return x * y

print multiply(3, 2)


# *args puts all arguments passed into a list.
def multiply_all(*args):
	result = 1
	for arg in args:
		result *= arg
	return result

print multiply_all(1, 2, 3, 4, 5)

# If positional arguments are specified first, those are required
# and Python will insert the first values into those arguments.
# The rest are optional and are placed in args.
def multiply_at_least_two(x, y, *args):
	result = x * y
	for arg in args:
		result *= arg
	return result

print multiply_at_least_two(1, 2, 3, 4, 5)

# *kwargs puts all named arguments into a dictionary.
def settings(**kwargs):
	for name, value in kwargs.items():
		print '{}: {}'.format(name, value)

# TODO: Call this with multiple key = value arguments.
settings(keyclicks = False, touchId = True, parrot = 'deceased')


# A common pattern in Python is to require one argument
# and to have optional keyword arguments.
def print_this(text, **kwargs):
	if 'reverse' in kwargs:
		print text[::-1]
	else:
		print text

print_this("test", reverse = True)


# And you can combine all of them.
def everything(x, *args, **kwargs):
	print "x =", x

	for arg in args:
		print arg

	for key, arg in kwargs.items():
		print "{}: {}".format(key, arg)

everything('spam')
everything('spam', 'swallow', 'coconut')
everything('spam', 'swallow', 'coconut', parrot = 'deceased')

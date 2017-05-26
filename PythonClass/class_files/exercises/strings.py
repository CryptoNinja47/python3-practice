# coding: utf-8

'''
Strings

Documentation:
	https://docs.python.org/2/tutorial/introduction.html#strings

'''

# Strings are text, a string of characters.
# Strings are always surrounded by single or double quotes:
spam = 'not much'
spam = "not much"

# There's no difference between single and double quotes except that you can avoid escaping the other kind of quote.
# That is, if you use double quotes and want a double quote in the string, you have to escape it:
spam = "not \"much\" spam in it"

# But using single quotes lets you have a double-quote in the string:
spam = 'not "much" spam in it'

# The preferred way to insert variables into strings is the .format() method.
# It's more readable and automatically gets the string equivalent of each argument.
language = "Python"
slogan = "{} is my number {} favorite".format(language, 1)
print slogan

# The string methods split() and join() are common ways to manipulate strings.
words = slogan.split()
print words

# The items are joined with whatever you specified as the separator between items.
print '-'.join(words)

# In Python, a string is considered a list.
# Being a list, all the standard list functionality works on strings.
for character in language:
	print character

print language[3]
print language[-1]

if 'Py' in language:
	print "Let's have Py!"

print language[2:5]

print len(language)

# Unlike standard lists, strings are immutable (that is, they can't be changed).
# That means that functions that appear to change strings actually return new strings.
text = "HELLO!"

print text.lower()	# This returns a new string, it doesn't change the original string.
print text

# A workaround for creating a string is to assign the changed string to the original variable.
text = text.lower()
print text

# Another way to "change" a string is to turn it into a list and change the list, 
# then turn it back into a string.
mylist = list(language)
mylist[2] = 'z'
language = ''.join(mylist)
print language


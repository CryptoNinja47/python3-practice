# coding: utf-8

'''
Regular Expressions


Regular expressions are a powerful mini-language for parsing text.
They simplify the process and can do things that would be very difficult and even impossible
using regular code.

This is just an introduction. If you find you need to use regular expressions, you should
read the full documentation.

Documentation:
	https://docs.python.org/2/library/re.html#module-re

'''

import re

'''
Find all the words that contain an 'o'.
'''
text = "The quick brown fox jumps over the lazy dog"

# The search function looks for the first occurrance of the pattern.
# It returns a match object or None.
# The match object's group() function shows the result.
result = re.search('o', text)
if result:
	print result.group()

# This regular expression looks for an 'o', then for any word characters after the 'o'.
# \w is 'word character' (letter or number), and * means 'zero or more' of them.
result = re.search(r'o\w*', text)
if result:
	print result.group()

# This regular expression looks for an 'o', then for any word characters on either side of the 'o'.
result = re.search(r'\w*o\w*', text)
if result:
	print result.group()

# The findall() function looks for all occurrences of the pattern.
# It returns a list of text that was found.
result = re.findall(r'\w*o\w*', text)
print result




'''
Find the sender of this email.
'''
line = "From: <Tim Cook> <Tuesday, 6/14/16>"


# We start by looking for text surrounded by angle brackets.
# The . is a regular expression that means "match any character", and the * means "zero or more".
result = re.search(r'From: <.*>', line)

# This gives us too much, all the way to the end of the line.
print result.group()

# That's because regular expressions are "greedy" -- by default they give you the longest possible answer.
# To make an expression non-greedy, use a ?.
result = re.search(r'From: <.*?>', line)
print result.group()

# That's better but it leaves the angle brackets as part of the result.
# To get rid of those, we can use parenthesis to specify a grouping we're interested in.
result = re.search(r'From: <(.*?)>', line)

# group() the complete match by default.
print result.group()

# To get our specific grouping, we can ask for group #1.
print result.group(1)

# You can define multiple groups in a single search.
result = re.search(r'From: <(.*?)> <(.*?)>', line)
print result.group(1)
print result.group(2)

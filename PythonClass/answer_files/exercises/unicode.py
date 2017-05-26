# coding: utf-8

'''
Unicode

For safety, always state the encoding of a Python file at the top of the file, as shown above.
That ensures that the text in the file will be read as utf-8. But it doesn't impact *anything* other
than how Python will read this .py file.

Unicode is:
	A bunch of numbers (code points) that map to characters (glyphs) in various languages.

UTF-8 is:
	Just one way of storing numbers. These numbers could be for anything, but for our purposes are 
	Unicode code points. The number determines which Unicode character to display.

UTF-8 is NOT Unicode:
	UTF-8 is just an encoding, just one way to store numbers. Unicode defines what the numbers mean.

The general strategy for handling Unicode is "The Unicode Sandwich":
	1. Read in text and convert it to Unicode. str.decode('<encoding>') converts text to Unicode.
	2. Use text within the script as Unicode.
	3. Convert Unicode to an encoded string (usually utf-8) before printing or writing it out. 
	   str.encode('<encoding') turns Unicode into an encoded string.

	You can use io.open(encoding='<encoding>') to convert text to Unicode as soon as it's read,
	and you can use io.open(encoding='<encoding>') to write out Unicode text as UTF-8.

Things to understand about ASCII, UTF-8, and Unicode:
	ASCII uses 7 bits, not 8.
	UTF-8 is not limited to 8 bits; it can handle up to 4 bytes for a character.

For a very readable summary of what everyone should know about Unicode and encodings, read:
	http://www.joelonsoftware.com/articles/Unicode.html

For a presentation on properly handling Unicode in Python, see:
	http://nedbatchelder.com/text/unipain.html	

'''

# The Movies.txt file is UTF-16, which results in either an error or characters represented as '?'
# when you use Python 2's open() function.
with open('data/Movies.txt') as myfile:
	contents = myfile.read()
print contents

'''
The Unicode Sandwich

1. Convert text to Unicode as it comes in.
2. Use Unicode in the body of your script.
3. Encode text as UTF-8 before outputting.

Why use the Unicode version of the text within the body of your script?
Because it's the truth.
'''
text = '€uro'
print len(text)		# 6

# The decode() function gets the Unicode version of the string.
uni = text.decode('utf-8')
print len(uni)		# 4


'''
These are examples of "The Unicode Sandwich" approach: Get text into Unicode as soon as possible, 
then encode it when you need to print or store the text.
'''

# Reading files with open():
with open('data/Movies.txt', 'r') as myfile:
	# 1. Read in text as bytes.
	contents = myfile.read()

	# 2. Convert the text to Unicode for use in the script. 
	uni = contents.decode('utf-16')
	print type(uni)

	# 3. Before printing or writing to disk, convert Unicode to an encoding:
	utf8 = uni.encode('utf-8')
	print type(utf8)
	print utf8


# Reading files with io.open(), which is the preferred approach as it immediately converts to Unicode.
# Also this is the equivalent of the Python 3 open() function.
import io
with io.open('data/Movies.txt', encoding = 'utf-16') as myfile:
	contents = myfile.read()
	print type(contents)


# Prefixing a string with 'u' treats it as Unicode:
text = u'ö'
print type(text)
#print text 	# This may or may not work depending on preferred encoding and other system settings.
print text.encode('utf-8')	# This is guaranteed to work.

# You can use \u to specify a Unicode code point.
text = u'\u00C6'

# A convenient way to print out a particular code point is to simply encode it.
print u'\u00C6'.encode('utf-8')


# unicodedata provides info for all codepoints.
import unicodedata as uni

char = u'\u1001'
print uni.name(char)
print char.encode('utf-8')	

# These look and should be treated the same, but they are not considered equal.
cafe1 = u'caf\u00E9' 		# composed "e" with acute accent
cafe2 = u'cafe\u0301' 		# decomposed "e" and acute accent
print cafe1 == cafe2

# Normalizing to composed characters ('NFD' is decomposed), and now they are the same.
c1 = uni.normalize('NFC', cafe1)
c2 = uni.normalize('NFC', cafe2)
print c1 == c2

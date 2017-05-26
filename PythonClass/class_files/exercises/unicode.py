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

with open('data/Movies.txt') as myfile:
	contents = myfile.read()
print contents


# TODO: Get the length of this utf-8 string, 
#       then use the string's decode() method to turn it into Unicode and get the length of that.
text = '€uro'


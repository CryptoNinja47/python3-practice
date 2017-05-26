# coding: utf-8

'''
TODO: 
	1. Use a for loop to open the 'names.txt' file for reading.
	2. Print "Hello <name>!" to each name listed in the file.

Every line in a file ends with a newline character (\n). Te remove the newline, you can use the string's rstrip() function.

'''



# For each name in 'names.txt',  print "Hello <name>!"
for line in open('names.txt', 'r'):
	# rstrip() removes whitespace, such as carriage returns, from the right side of the string.
	print "Hello {}!".format(line.rstrip())

# coding: utf-8

'''
TODO:
    1. Use a for loop to open the 'names.txt' file for reading.
    2. Print "Hello <name>!" to each name listed in the file.

Every line in a file ends with a newline character (\n).
Te remove the newline, you can use the string's rstrip() function.

'''
for line in open('./data/names.txt', 'r'):
    print "Hello {}!".format(line.rstrip()) # rstrip() remove whitespace characters

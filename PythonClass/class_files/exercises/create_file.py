# coding: utf-8

'''
TODO:
    1. Create a list of names.
    2. Open the file for writing using a 'with' block.
       The 'with' block closes the file when the block is done.
    3. Using a for loop, write each name to the file 'names.txt'.
       Use the file's write() command to write text to the file.

Whenever you are working with a file, you always start by calling open() to access the file.

The first argument to open() is the path to the file, the second is a letter indicating what you are going to do with the file:

    File modes:
           'w' = write
           'r' = read
           'a' = append

When writing to the file, you have to add a newline (\n) at the end of a line.

'''

NAMES = ['Dave', 'Bob', 'Grace', 'Mary']
with open('./data/names.txt', 'w') as myfile:
    for name in NAMES:
        myfile.write(name + '\n')

# coding: utf-8

'''
Files

Documentation:
	https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files

File modes: 
	'w' = write    
	'r' = read
    'a' = append

'''

names = ['Francis', 'Grace', 'Matt', 'Zanetta']

# The open() function is used for file handling.
# The second argument indicates what you are going to do to the file.
# 'w' is write mode, which creates the file if necessary and deletes any existing content.
myfile = open('names.txt', 'w')

for name in names:
	myfile.write(name + '\n')

# When you open a file, you must also close it when done with it, 
# to ensure changes are flushed to disk and to free it up for use by others.
myfile.close()


# Now that we've written out the file, let's open it and read the contents.
# You should never read in all file contents at once like this unless you know
# the file will be small.
myfile = open('names.txt', 'r')
contents = myfile.read()
myfile.close()
print contents

# In most cases, you want to read a file one line at a time, which you can do with a for loop.
# When opening the file as part of the for loop, the file will be closed automatically for you
# at the end of the loop.
for line in open('names.txt', 'r'):
	print line

# The with statement will also close the file automatically after the code block.
with open('names.txt', 'a') as myfile:
	myfile.write('Ron\n')
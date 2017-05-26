# coding: utf-8

'''
TODO: 
	1. Create a function called sort_by_filename() that takes a path and returns the filename.
		- Hint: You can use the string's split() function to split the path on the '/' character.

	2. Use sorted() to print a sorted copy of the list, using sort_by_filename as the sorting function.
'''

paths = ['PythonClass/exercises/variadic.py',
         'PythonClass/exercises/comprehensions.py',
         'PythonClass/exercises/hello.py',
         'PythonClass/exercises/exceptions.py',
         'PythonClass/exercises/directory_iterator.py']


def sort_by_filename(path):
	segments = path.split('/')
	filename = segments[-1]
	return filename

print sorted(paths, key = sort_by_filename)



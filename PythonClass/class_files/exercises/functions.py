# coding: utf-8
''' Useful functions for the Python classs. '''
'''
TODO:
    1. Create a function called words().
    2. The function should take a text argument,
       and use the string's split() function to return a list of the words found in the text.

The syntax for defining a function is:

    def func_name(argument1, argument2):
        # code
        return result
'''

def get_words(arg1):
    '''This is my test function'''
    words = arg1.split()
    count = len(words)
    return words, count

# print get_words('Hello monty python')


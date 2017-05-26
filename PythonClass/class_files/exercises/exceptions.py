# coding: utf-8

'''
Exceptions

Documentation:
	https://docs.python.org/2.7/tutorial/errors.html#exceptions

'''


'''
TODO: Put the flaky() function call inside an exception handler.
      If a FlakyError exception is encountered, print a message and re-raise the exception.
'''
from utilities import flaky, FlakyError

flaky()
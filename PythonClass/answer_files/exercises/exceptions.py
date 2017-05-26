# coding: utf-8

'''
Exceptions

Documentation:
	https://docs.python.org/2.7/tutorial/errors.html#exceptions

'''

import os

numbers = range(5)

try:
	number = numbers[10]
except IndexError as e:
	print "Handling index error:", e
except Exception as e:
	print "Exception:", type(e), e
else:
	print "No exception, so now doing this..."
finally:
	print "This is called no matter what. Cleaning up..."

print "Continuing..."



'''
Two philosophies of exception handling

LBYL: Look Before You Leap

EAFP: It's Easier to Ask Forgiveness than Permission
'''

# LBYL looks like this, checking first that the call will be valid:
path = '/usr/bin'
if not os.path.exists(path):
	print "File doesn't exist, so calling os.mkdir() to create it..."

	'''
	But wait, between the time we checked and now, 
	the path might have been created, and mkdir() will return
	an exception when we try to create it again.
	'''
	# os.mkdir(path)	# OSError: [Errno 17] File exists: '/usr/bin'
	print "Oops, bad idea."


# EAFP uses exception to simplify,
# and to remove race conditions between the time you check and the time you actually do it.
try:
	os.mkdir(path)
except OSError:
	print "Path already exists so we got an exception. No problem!"


'''
TODO: Put the flaky() function call inside an exception handler.
      If a FlakyError exception is encountered, print a message and re-raise the exception.
'''
from utilities import flaky, FlakyError

try:
	flaky()
except FlakyError as e:
	print "Flakiness detected, can't recover:", e
	raise
except Exception as e:
	print "Got exception of type:", type(e)
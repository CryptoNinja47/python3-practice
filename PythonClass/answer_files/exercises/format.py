# coding: utf-8

'''
String formatting

String formatting is both simple and powerful.

Documentation:
	https://pyformat.info
'''
# In the simplest form, use the string.format() method to interpolate values.
myString = "The {} brown fox jumps over the {} dog".format("quick", "lazy")
print myString

# If you think of the string as a re-usable template, it becomes more powerful.
# Remember that since strings are immutable, the format method returns a new version of the
# string, leaving the original template as-is.
template = "The {} brown fox jumps over the {} dog"
first = template.format("careless", "ambivalent")
second = template.format("bad", "delighted")
print first
print second

# The template can have named values, letting you assign them in any order.
# In this case you are required to provide the named arguments.
template = "The {fox_type} brown fox jumps over the {dog_type} dog"
first = template.format(dog_type="spotted", fox_type="springy")
print first

# You can specify an index order (starts with 0) for the arguments.
template = "The {1} brown fox jumps over the {0} dog"
first = template.format("lazy", "quick")
print first

# Using either named values or index order, you can then have the template access a dictionary item.
template = "The {0[fox_type]} brown fox jumps over the {1[dog_type]} dog"
myDict = {"fox_type": "little", "dog_type": "rotund"}
first = template.format(myDict, myDict)
print first

# You can also call a method.
import sys
template = "You are running on {0.platform}"
first = template.format(sys)
print first
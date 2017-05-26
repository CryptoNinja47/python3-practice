# coding: utf-8

'''
Lists

Lists have an order to their items, and are changeable (mutable).

Documentation:
	https://docs.python.org/2/tutorial/introduction.html#lists
'''


# Square brackets create an empty list.
animals = []

# The append() function adds an item to the end of the list.
animals.append('cat')
animals.append('frog')
animals.append('bird')

# To access an item in the list, indicate the item number in brackets.
# Python lists are zero-based, meaning the first item is item #0.
first = animals[0]

# Negative numbers index from the end of the list, so -1 is the last item in the list.
last = animals[-1]

# You can change an item in the list.
animals[1] = 'swallow'


# To check for an item in the list, use 'if in'.
if 'dog' in animals:
	print 'Found a dog!'
elif 'bird' in animals:
	print 'Found a bird!'
else:
	print 'Found nothing!'

# You can also check for something not being in the list.
if 'cow' not in animals:
	print "Where's the beef?"

# Use the len() function to get the count of any kind of list.
count = len(animals)

if count > 2:
	print "That's a lot of animals!"

# If you provide the same number of variables as are in the list, 
# Python will unpack the list items into the variables.
first, second, third = animals
print first


'''
Loops

Python supports for loops and while loops, and standard loop control flow statements.
'''
products = ['iPad', 'Watch', 'iMac', 'Music']

# A for loop is constucted as:
# 	for variablename in listname:
# The variablename can be any name you like. 
# Python iterates through the list; each time through, the variablename points to the current item.
for spam in products:
	print spam

# The range() function creates a list of numbers you can loop through
# to do an operation a specific number of times.
for index in range(4):
	print index, products[index]

# A while loop continues as long as the while statement is True.
count = 0
while count < 3:
	print products[count]
	count += 1


# The break statement breaks out of the nearest loop and continues on to the next line.
# "while True" creates an infinite loop...until you break out of it.
count = 0
while True:
	print products[count]
	count += 1
	if count == len(products):
		break
print "Done!"


# The continue statements causes the nearest loop to move on to the next item in the list.
for product in products:
	if product.startswith('i'):
		# 'i' is so 2001! Let's skip it.
		continue
	print product

# The range() function returns a list of numbers in the specified range.
numbers = range(10)
print numbers

# Slicing is how you can get a subset of a list.
# The slice goes from the starting number up to the ending number.
print numbers[2:7]
print numbers[2:-1]		# You can use a negative index to indicate the ending item.
print numbers[:7]		# This starts at the beginning of the list.
print numbers[3:]		# This goes to the end of the list.
print numbers[:]		# This gives a copy of the list. Don't do this -- use list() instead to make a copy.





'''
List sorting

The sorted() and sort() functions take the same arguments for customizing the sorting.
'''

# sorted() returns a sorted copy of the list, useful when you don't want to change the original list.
print sorted(animals)
print sorted(animals, reverse = True)

# The sort() function is the same as sorted(), except it changes the list.
animals.sort()
print animals

# The 'key' argument lets you indicate what function to use to do the sorting.
# Specifying 'len' as the key sorts based on the length of the strings.
print sorted(animals, key = len)
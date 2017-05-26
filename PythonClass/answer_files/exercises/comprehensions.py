# coding: utf-8

'''
Comprehensions

Comprehensions are a flattened for loop. They are efficient and easy to read, 
and considered more 'Pythonic' than using map/filter/reduce.

Documentation:
	https://docs.python.org/2.7/tutorial/datastructures.html#list-comprehensions

'''

# For loop for collecting a list of numbers
numbers = []
for number in range(10):
	numbers.append(number)
print numbers

# Comprehension:
print [number for number in range(10)]



# For loop for creating a list of doubled numbers.
doubled = []
for number in range(10):
	doubled.append(2 * number)
print doubled

# Comprehension:
print [number * 2 for number in range(10)]



# For loop for printing the middle row of a matrix.
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
middle = []
for row in matrix:
	middle.append(row[1])
print middle

# Comprehension:
print [row[1] for row in matrix]


print [matrix[i][i] for i in range(len(matrix))]

# Filtering in a comprehension
print [num for num in range(10) if num % 2 == 0]
print [num for num in range(10) if num % 2 == 0 and num > 5]
print [num for num in range(10) if num % 2 == 0 or num > 5]



# Dictionary comprehension
animals = ["dogs", "cats", "birds"]
counts = [10, 8, 32]
animal_dict = {animals[i] : counts[i] for i in range(len(animals))}


# The map/filter/reduce exercise done as comprehensions...
import csv
from collections import namedtuple
Store = namedtuple('Store', 'state, city, neighborhood')

stores = [Store._make(row) for row in csv.reader(open('data/us_stores.csv'))]

florida_stores = [store for store in stores if store.state == 'Florida']

total = len(florida_stores)

print "There are {} stores in Florida.".format(total)



from pprint import pprint

# TODO: Include this?
# Cartesian product -- comprehension using multiple for loops.
colors = ['black', 'white']
sizes = ['S', 'M', 'L'] 

combos = []
for color in colors:
	for size in sizes:
		combos.append((color, size))	

pprint(combos)

combos = [ (color, size) for color in colors for size in sizes ]
pprint(combos)



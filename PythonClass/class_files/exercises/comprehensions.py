# coding: utf-8

'''
Comprehensions

'''


# TODO: For each of the for loops below, enter the comprehension equivalent.

# For loop for collecting a list of numbers
numbers = []
for number in range(10):
	numbers.append(number)
print numbers

# Comprehension:


# For loop for creating a list of doubled numbers.
doubled = []
for number in range(10):
	doubled.append(2 * number)
print doubled

# Comprehension:


# For loop for printing the middle row of a matrix.
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
middle = []
for row in matrix:
	middle.append(row[1])
print middle

# Comprehension:


# Dictionary comprehension
animals = ["dogs", "cats", "birds"]
counts = [10, 8, 32]
animal_dict = {animals[i] : counts[i] for i in range(len(animals))}


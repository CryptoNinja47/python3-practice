# coding: utf-8

nums = range(101)

# Third slicing argument is a skip (stride) amount.
print nums[::20]

# Reverse skipping works.
print nums[::-20]

text = 'spaceship'
print text[::-1]

# There is a slice object, which makes it possible to give names to slices.
backwards = slice(None, None, -1)
print text[backwards]

alternating = slice(None, None, 2)
print text[alternating]

five = slice(None, 6)
print text[five]



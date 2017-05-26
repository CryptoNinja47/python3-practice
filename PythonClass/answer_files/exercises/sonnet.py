# coding: utf-8

'''
TODO: Determine how many words are in the file 'data/Sonnet.txt'

Hints:
- Working with files always requires calling open().
- To be safe it's best to read in one line at a time using a for loop.
- The string method split() will be helpful.
'''

total = 0
for line in open('data/Sonnet.txt'):
	words = line.split()
	count = len(words)
	total += count

print total

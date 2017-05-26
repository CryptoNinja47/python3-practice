# coding: utf-8

'''
TODO: Read in the spreadsheet of US Apple stores ('data/us_stores.csv') and print out 
      the store locations in this format:

	State: City (neighborhood)

	For example:

	Mississippi: Ridgeland (Renaissance at Colony Park)
'''

for row in open('data/us_stores.csv', 'r'):
	row = row.rstrip()
	items = row.split(',')
	state, city, neighborhood = items
	print "{}: {} ({})".format(state, city, neighborhood.lstrip())
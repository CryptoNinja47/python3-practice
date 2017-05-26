# coding: utf-8

'''
TODO: Now read in the spreadsheet of Apple stores ('data/apple_stores_notes.csv') using the csv module 
      and print out the number of stores in each country, sorted by the number:

	Country: # stores
'''
import csv

countries = {}

with open('data/apple_stores.csv') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		country = row[0]
		if country not in countries:
			countries[country] = 1
		else:
			countries[country] += 1

def sort_by_num_stores(sort_item):
	return sort_item[1]

for country, num_stores in sorted(countries.items(), key = sort_by_num_stores, reverse = True):
	print "{}: {} stores".format(country, num_stores)

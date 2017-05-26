# coding: utf-8

'''
TODO: Parse the Apache weblog in 'data/access_log.txt' and produce a report. 

1: Print out how many web hits we've gotten. Each line in the file is a web hit.

2. Print out how many times each URL has been hit.
'''

# coding: utf-8

'''
TODO: Parse the Apache weblog in 'data/access_log.txt' and produce a report. 

1: Print out how many web hits we've gotten. Each line in the file is a web hit.

2. Print out how many times each URL has been hit.
'''
import re
import utilities

# 64.242.88.10 - - [07/Mar/2004:16:24:16 -0800] "GET /twiki/bin/view/Main/PeterThoeny HTTP/1.1" 200 4924

count = 0
for line in open('data/access_log.txt', 'r'):
	if "GET " in line:
		count += 1

urls = {}
for line in open('data/access_log.txt', 'r'):
	result = re.search(r'GET (.*?) ', line)
	if result:
		url = result.group(1)
#		urls[url] = urls.get(url, 0) + 1

		if url not in urls:
			urls[url] = 1
		else:
			urls[url] += 1

def sort_by_value(key_value_tuple):
	return key_value_tuple[1]

sorted_urls = sorted(urls.items(), key = sort_by_value, reverse = True)

utilities.write_report(count, sorted_urls)
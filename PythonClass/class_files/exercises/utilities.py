# coding: utf-8

'''
Useful functions for the Python Basics class.
'''
# For the regular expression module, emulating a line from a mail file.
message = "From: <Tim Cook> <Tuesday, 6/14/16>"

import subprocess
def write_report(hits = 0, top_urls = []):
	'''
	For the log analyzer exercise, this function writes out data/website_report.html using the provided values,
	and opens the file in a browser.
	'''
	html = open("data/report_template.html", "r").read()
	
	html = html.replace('[hits]', str(hits))

	top_urls_text = '<table><tr><th>URL</th><th>hits</th></tr>\n'
	for url, hits in top_urls:
		top_urls_text += '<tr><td>{}</td><td>{}</td></tr>\n'.format(url, hits)
	top_urls_text += '</table>'
	html = html.replace('[top_urls]', top_urls_text)
		
	with open("data/website_report.html", "w") as output:
		output.write(html)

	subprocess.call(["open", "data/website_report.html"])


from collections import namedtuple
Movie = namedtuple('Movie', 'title, year, director, revenue')

# A function that returns an exception, for use in the exceptions exercise.
class FlakyError(Exception):
	def __init__(self, code):
		self.code = code

	def __str__(self):
		return "Flaky type #{}. Don't call flaky functions!".format(self.code)

def flaky():
	import random
	raise FlakyError(random.choice(range(100)))
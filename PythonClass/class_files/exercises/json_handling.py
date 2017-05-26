# coding: utf-8

'''
JSON 

Important: 
	*DON'T* create a file called json.py, or you will break the json handling.
	Why? Because your json.py will override the built-in json file, and it 
	will be very difficult to figure out why nothing works.
	(Yes, I have done this more than once...)
'''

import sys
import getpass 		# For getting password without displaying the text
import json
from pprint import pprint

import requests		# sudo -H pip install requests

user = raw_input("Open Directory username: ")

try:
	password = getpass.getpass()
except Exception as e:
	sys.exit("\nUnable to continue without password.")

url = 'https://directory.swe.apple.com/services/people/' + user

r = requests.get(url, auth=(user, password))

results = json.loads(r.text)

pprint(results)

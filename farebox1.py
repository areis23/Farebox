"""
A program to test importing of farebox output data
"""

import csv

# print row with highest farebox recovery
"""
with open('temp.txt', 'rb') as csvfile:
	fb_reader = csv.DictReader(csvfile, delimiter=',')
	max_rec = 0
	num = 0
	for i,j in enumerate(fb_reader):
		if j['FAREBOX_RECOVERY'] > max_rec:
			max_rec = j['FAREBOX_RECOVERY']
			num = i

with open('temp.txt', 'rb') as csvfile:
	fb_reader = csv.DictReader(csvfile, delimiter=',')
	for i,j in enumerate(fb_reader):
		if i == num:
			print j
"""

with open('temp.txt', 'rb') as csvfile:
	fb_reader = csv.DictReader(csvfile, delimiter=',')
	cumberland_fare = 0.0
	for i,j in enumerate(fb_reader):
		if j['COUNTY'] == 'Cumberland':
			cumberland_fare += float(j['FARE_COLLECTED'])
	print cumberland_fare
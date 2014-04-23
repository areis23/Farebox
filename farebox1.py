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
#add up fare collected for Cumberland County
"""
with open('temp.txt', 'rb') as csvfile:
	fb_reader = csv.DictReader(csvfile, delimiter=',')
	cumberland_fare = 0.0
	for i,j in enumerate(fb_reader):
		if j['COUNTY'] == 'Cumberland':
			cumberland_fare += float(j['FARE_COLLECTED'])
	print cumberland_fare
"""

# create dict of counties with fare and cost totals
with open('temp.txt', 'rb') as csvfile:
	fb_reader = csv.DictReader(csvfile, delimiter=',')
	counties = []
	stats = {}
	print "County        Fare Collected    Cost"
	print 
	for i in fb_reader:
		if i['COUNTY'] not in counties:
			counties.append(i['COUNTY'])
			stats[i['COUNTY']] = (float(i['FARE_COLLECTED']), float(i['TOTAL_OPERATING_COST']))
		else:
			stats[i['COUNTY']] = (stats[i['COUNTY']][0] + float(i['FARE_COLLECTED']), stats[i['COUNTY']][1] + float(i['TOTAL_OPERATING_COST']))
	counties.sort()
	for item in (counties):
		print item + ":       " + str(stats[item][0]) + "  " + str(stats[item][1])


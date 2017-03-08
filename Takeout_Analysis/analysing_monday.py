#!/usr/bin/python
import datetime
import os
import glob
import csv
extension = 'csv'

result = [i for i in glob.glob('*.{}'.format(extension))]
#print(result)
dict1 = {}
dict2 = {}
dict3 = {}
dict4 = {}
dict5 = {}
dict6 = {}
dict7 = {}
counter = [0,0,0,0,0,0,0]
mydict = {}
for file in result:
	cur = file[:10]
	y = int(cur[:4])
	m = int(cur[5:7])
	d = int(cur[8:10])
	date = datetime.date(y,m,d)
	weekday = date.weekday()
	if weekday == 0:
		for entry in csv.DictReader(open(file), delimiter='\t'):
			x = entry.values()[0]
			y = x.split(",")
			mydict[y[0]]= y[3]
			time = y[0]
			abstime = time[:2]
			if y[3] != "" and y[3] != " ":
				if abstime in dict1:
					dict1[abstime] = dict1[abstime] + float(y[3])
				else:
					dict1[abstime] = float(y[3])				
	elif weekday == 1:
		for entry in csv.DictReader(open(file), delimiter='\t'):
			x = entry.values()[0]
			y = x.split(",")
			mydict[y[0]]= y[3]
			time = y[0]
			abstime = time[:2]
			if y[3] != "" and y[3] != " ":
				if abstime in dict2:
					dict2[abstime] = dict2[abstime] + float(y[3])
				else:
					dict2[abstime] = float(y[3])	
	elif weekday == 2:
		for entry in csv.DictReader(open(file), delimiter='\t'):
			x = entry.values()[0]
			y = x.split(",")
			mydict[y[0]]= y[3]
			time = y[0]
			abstime = time[:2]
			if y[3] != "" and y[3] != " ":
				if abstime in dict3:
					dict3[abstime] = dict3[abstime] + float(y[3])
				else:
					dict3[abstime] = float(y[3])
	elif weekday == 3:
		for entry in csv.DictReader(open(file), delimiter='\t'):
			x = entry.values()[0]
			y = x.split(",")
			mydict[y[0]]= y[3]
			time = y[0]
			abstime = time[:2]
			if y[3] != "" and y[3] != " ":
				if abstime in dict4:
					dict4[abstime] = dict4[abstime] + float(y[3])
				else:
					dict4[abstime] = float(y[3])
	elif weekday == 4:
		for entry in csv.DictReader(open(file), delimiter='\t'):
			x = entry.values()[0]
			y = x.split(",")
			mydict[y[0]]= y[3]
			time = y[0]
			abstime = time[:2]
			if y[3] != "" and y[3] != " ":
				if abstime in dict5:
					dict5[abstime] = dict5[abstime] + float(y[3])
				else:
					dict5[abstime] = float(y[3])				
	elif weekday == 5:
		for entry in csv.DictReader(open(file), delimiter='\t'):
			x = entry.values()[0]
			y = x.split(",")
			mydict[y[0]]= y[3]
			time = y[0]
			abstime = time[:2]
			if y[3] != "" and y[3] != " ":
				if abstime in dict6:
					dict6[abstime] = dict6[abstime] + float(y[3])
				else:
					dict6[abstime] = float(y[3])				
	elif weekday == 6:
		for entry in csv.DictReader(open(file), delimiter='\t'):
			x = entry.values()[0]
			y = x.split(",")
			mydict[y[0]]= y[3]
			time = y[0]
			abstime = time[:2]
			if y[3] != "" and y[3] != " ":
				if abstime in dict7:
					dict7[abstime] = dict7[abstime] + float(y[3])
				else:
					dict7[abstime] = float(y[3])
	counter[weekday] = counter[weekday] + 1								
alltimes = sorted(dict1.keys())
#print alltimes
for x in alltimes:
	print x + "\t" + str(int(dict1[x])/counter[0]) + "\t" + str(int(dict2[x])/counter[1]) + "\t" + str(int(dict3[x])/counter[2]) + "\t" + str(int(dict4[x])/counter[3]) + "\t" + str(int(dict5[x])/counter[4]) + "\t" + str(int(dict6[x])/counter[5]) + "\t" + str(int(dict7[x])/counter[6])
#print counter	
#for key in dict1:print key + "\t" + str(int(dict1[key]))









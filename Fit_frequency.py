#!/usr/bin/python
import datetime
import csv
mydict = {}
for entry in csv.DictReader(open("Daily_Summaries.csv"), delimiter='\t'):
	x = entry.values()[0]
	y = x.split(",")
	mydict[y[0]]= y[2]

#print mydict
newdict = {}
for a in range(7):
	newdict[a] = 0
for x in mydict:
#	print x
	a = x[:6] + "20" + x[6:]
	date = datetime.datetime.strptime(a, "%d/%m/%Y")
	weekday = date.weekday()
	if(mydict[x]!=" " and mydict[x]!=""):
		newdict[weekday] = int(newdict[weekday]) + float(mydict[x])
print newdict

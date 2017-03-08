#!/usr/bin/python
import datetime
import json
from urlparse import urlparse
import matplotlib.pyplot as plt
import operator
import tldextract
import datetime
domain_freq = {}
domain_freq_top_20 = {}
weekwise = {}
weeklyfinal = weekwise
daily = {}
with open("BrowserHistory.json") as chrome_history:
	data = json.load(chrome_history)
for mylist in data.values()[0]:
	cur = mylist.get("url")
	usectime = mylist.get("time_usec")
	usectime = usectime/1000000
	time = datetime.datetime.fromtimestamp(usectime)
	day_of_week = time.weekday()
	parsed_url = urlparse(cur)
	domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_url)
	if domain in domain_freq:
		domain_freq[domain] = domain_freq[domain] + 1
	else:
		domain_freq[domain] = 1
sorted_vals = sorted(domain_freq.values(), reverse = True)
top_20 = sorted_vals[20]
for k in domain_freq:
	if(domain_freq[k] > top_20):
		domain_freq_top_20[k] = domain_freq[k]
list1 = []
list2 = []
newdomain = {}
i = 0
for k in domain_freq_top_20:
	list1.append(tldextract.extract(k))
	list2.append(domain_freq_top_20[k])
del domain_freq_top_20['https://zestmoney.mambu.com/']
del domain_freq_top_20['http://zestmoney.gogetspeedy.com/']
del domain_freq_top_20['chrome://newtab/']
for x in range(len(list1)):
	newdomain[list1[x].domain] = list2[x]
del newdomain['mambu']
del newdomain['gogetspeedy']
del newdomain['newtab']
for i in newdomain:
	weekwise[i] = {}
	daily[i] = {}
for x in weekwise:
	for a in range(7):
		weekwise[x][a]=0	
for x in daily:
	daily[x]["morning"] = 0
	daily[x]["afternoon"] = 0
	daily[x]["evening"] = 0
	daily[x]["night"] = 0
for mylist in data.values()[0]:
	cur = mylist.get("url")
	usectime = mylist.get("time_usec")
	usectime = usectime/1000000
	time = datetime.datetime.fromtimestamp(usectime)
	day_of_week = time.weekday()
	hour = time.hour
	parsed_url = urlparse(cur)
	domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_url)
	domain = tldextract.extract(domain).domain
	if (domain in weekwise):
		weekwise[domain][day_of_week] = weekwise[domain][day_of_week] + 1
	if (domain in daily):
		if 22 <= hour or hour < 7:
			daily[domain]["night"] = daily[domain]["night"] + 1
		elif 7 <= hour < 12:
			daily[domain]["morning"] = daily[domain]["morning"] + 1
		elif 12 <= hour < 17:
			daily[domain]["afternoon"] = daily[domain]["afternoon"] + 1
		elif 17 <= hour < 22:
			daily[domain]["evening"] = daily[domain]["evening"] + 1
for key in weekwise:
	print "{State:" + key + ",freq:" + str(weekwise[key])+"},"
for key in daily:
	print "{State:" + key + ",freq:" + str(daily[key])+"},"

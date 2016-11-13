

import os
import csv
import glob

subs = []

for file in glob.glob('*2016*csv'):
	with open(file,'r') as csvfile:
		reader = csv.reader(csvfile,delimiter=',')
		for row in reader:
			subs.append(row[12])

count = len(subs)
subcount = subs.count('Subscriber')

print count
print subcount
print "%0.2f percent of users are subscribers" % (float(subcount)/float(count)*100)

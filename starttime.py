

import os
import csv
import glob
from datetime import datetime

timeformat = '%m/%d/%Y %H:%M:%S'

starttimes = []

for file in glob.glob('*2016*csv'):
	with open(file,'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		next(reader)
		for row in reader:
			starttimes.append(datetime.strptime(row[2],timeformat))


weekdaytimes = [t for t in starttimes if t.isoweekday() in range(1,6)]

hours = {}
for i in range(24):
	hours[i] = 0

for t in weekdaytimes:
	hours[t.hour] += 1

print hours

pophour = max(hours, key=hours.get)
print pophour



			



import os
import csv
import glob
from datetime import datetime

timeformat = '%m/%d/%Y %H:%M:%S'

start = []
end = []


for file in glob.glob('*2016*csv'):
	with open(file,'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		next(reader)
		for row in reader:
			start.append(row[4])
			end.append(row[8])


start_count = {}
end_count = {}
for station in set(start):
	start_count[station] = start.count(station)
	end_count[station] = end.count(station)

deltas = {}
for key,val in start_count.items():
	deltas[key] = end_count[key] - start_count[key]

heavyend = max(deltas, key=deltas.get)
heavystart = min(deltas, key=deltas.get)

print "The most unbalanced stating station is %s with %d more stating than ending" % (heavystart, abs(deltas[heavystart]))
print "The most unbalanced ending station is %s with %d more ending than starting" % (heavyend, abs(deltas[heavyend]))

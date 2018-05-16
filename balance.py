#!/usr/bin/env python3


import os
import csv
import glob
from datetime import datetime

timeformat = '%m/%d/%Y %H:%M:%S'

start = []
end = []


for file in glob.glob('*2016*csv'):
	print(file)
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
for key in start_count:
	deltas[key] = end_count[key] - start_count[key]

heavyend = max(deltas, key=deltas.get)
heavystart = min(deltas, key=deltas.get)

print('The most unbalanced stating station is {} with {} more stating than ending'.format(heavystart, abs(deltas[heavystart])))
print('The most unbalanced ending station is {} with {} more ending than starting'.format(heavyend, abs(deltas[heavyend])))


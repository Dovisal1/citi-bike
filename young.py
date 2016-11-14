

import os
import csv
import glob
from datetime import datetime
import pandas as pd
import numpy as np

timeformat = '%m/%d/%Y %H:%M:%S'

station = []
birth = []


print "reading"
for file in glob.glob('*2016*csv'):
	with open(file,'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		next(reader)
		for row in reader:
			try:
				birth.append(int(row[13]))
				station.append(row[4])
			except:
				continue

d = {'station' : station, 'age' : birth}

df = pd.DataFrame(d)

means = df.groupby(['station']).mean()


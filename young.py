

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
			station.append(row[4])
			birth.append(row[13])

d = {'station' : station, 'age' : birth}

df = pd.DataFrame(d)

means = df.groupby(['station']).mean()


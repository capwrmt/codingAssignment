#!/usr/bin/env python

import csv
from collections import namedtuple
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("always")
import matplotlib.ticker as mtick

'''
1. Read in CSV File into array 
2. Calculate time to last byte (req time + transfer time + turnaround time)
3. Group distribution into object size classes - algorithm / data structure
4. Graph in a bar chart using pychart

Todos:
Error checking via Try-except
'''
Msg = namedtuple('Msg', ('http_status', 'obj_sz', 'req_time', 'transfer_time', 'ts', 'turn_time'))

data = []

count = 0 # Count total number of rows in CSV
'''
with open('exercise.log.csv') as csv_file:
	reader = csv.reader(csv_file)
	for row in reader:
		data.append(Msg(*row))
		count +=1
'''

d = pd.read_csv('exercise.log.csv')
d['ttlb'] = d['req_time'] + d['transfer_time'] + d['turn_time']

dS = d[(d['obj_sz'] <= 100)]
dS2 = d[(d['obj_sz'] > 100) & (d['obj_sz'] < 10000)]
print(dS)
print(dS2)
# TODO: Slice the data into the obj_sz buckets

#obj_sz=d['obj_sz']

legend = ['>100M<1G','>10M<100M','<100K','>1M<10M','>100K<1M']
plt.hist(([dS['ttlb']], [dS2['ttlb']]), bins='auto', normed=True, alpha=.5)
plt.xlabel("TTLB in ms (logarithmic scale base 2")
plt.ylabel("% of TTLB times in sample")
plt.legend(legend)
#plt.xticks(range(1, 33554432))
#plt.yticks(range(0, 14))
#plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(xmax=100))
	
plt.title('Time To Last Byte Distribution Per Object Size Class')
#plt.yscale('log', basey=2, nonposy='clip')
#plt.xscale('log', basex=2, nonposy='clip')
plt.show()


#print(d['obj_sz']
#print count	# debug to check that all rows are read	


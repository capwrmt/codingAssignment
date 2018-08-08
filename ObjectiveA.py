#!/usr/bin/env python

import csv
import matplotlib.pyplot as plt
from collections import namedtuple

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
with open('exercise.log.csv') as csv_file:
	reader = csv.reader(csv_file)
	for row in reader:
		data.append(Msg(*row))
		count +=1

legend = ['>100M<1G','>10M<100M','<100K','>1M<10M','>100K<1M']
plt.hist([score_india, score_pk], color=['orange', 'green'])
plt.xlabel("TTLB in ms (logarithmic scale base 2")
plt.ylabel("% of TTLB times in sample")
plt.legend(legend)
plt.xticks(range(1, 33554432))
plt.yticks(range(0, 14))
plt.title('Time To Last Byte DistributionPer Object Size Class')
plt.show()

print count	# debug to check that all rows are read	


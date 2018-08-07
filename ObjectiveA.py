#!/usr/bin/env python

import csv
# Import `pyplot` from `matplotlib`
import matplotlib.pyplot as plt

'''
1. Read in CSV File into array 
2. Calculate time to last byte (req time + transfer time + turnaround time)
3. Group distribution into object size classes
4. Graph in a bar chart using pychart

Todos:
Error checking via Try-except
'''

f = open('exercise.log.csv')

data = []
count = 0 # Count total number of rows in CSV

# Iterate through each row in CSV file
# But first store the header
header_line = next(f)
for row in f:
	data_row = row.rstrip().split('\t')
	data.append(data_row)
	count += 1
'''
	if 

	elif

	else
'''
#print data
print count

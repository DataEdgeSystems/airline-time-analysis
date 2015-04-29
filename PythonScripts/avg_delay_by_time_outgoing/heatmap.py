#!/usr/bin/env python
"""
Generate the heat map using the previously computed data for avg depart delay by time

@author Luigi Patruno
@date 29 Apr 2015
"""

file_path = '../../data/avg_delay_by_time_outgoing/part-00000'

data = []

f = open(file_path)
for line in f:
    key, val = line.strip().split('\t')
    (month, day, time) = (x for x in key.split('_'))
    if len(time) == 3:
	hour, minute = time[0], time[1:]
    else:
	hour, minute = time[:2], time[2:]
    data.append( [int(month), int(day), int(hour), int(minute), float(val) ] )

data = sorted(data, key = lambda x: (x[0], x[1], x[2], x[3]) )

num_rows = len(data)


print data
f.close()

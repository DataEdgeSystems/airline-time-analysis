#!/usr/bin/env python
"""
Reducer to get the mean arrival delay and number of flights per trip for incoming flights to JFK

Emit (origin_JFK, mean arrival delay_num trips)

@author Luigi Patruno
@date 28 Apr 2015
"""
import sys

last_key = None
num_trips = 0
arrival_delay = []

for line in sys.stdin:
    key, val = line.strip().split('\t')

    if last_key and last_key != key:
	avg_delay = sum(arrival_delay) / len(arrival_delay)
        num_trips = len(arrival_delay)
	last_val = '%.3f_%d' % (avg_delay, num_trips)
        print '%s\t%s' % (last_key, last_val)
        last_key = key
	if val != 'NA':
	    arrival_delay = [ float(val) ]
	else:
	    arrival_delay = []
    else:
        last_key = key
	if val != 'NA':
	    arrival_delay.append( float(val) )

# Don't forget to print the last set
if last_key:
    avg_delay = sum(arrival_delay) / len(arrival_delay)
    num_trips = len(arrival_delay)
    last_val = '%.3f_%d' % (avg_delay, num_trips)
    print '%s\t%s' % (last_key, last_val)



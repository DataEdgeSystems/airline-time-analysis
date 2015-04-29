#!/usr/bin/env python
"""
Reducer to get the mean departure delay by day of the year and time of day flights departing from JFK

Emit (month_day_timebin, mean departure delay)

@author Luigi Patruno
@date 28 Apr 2015
"""
import sys

last_key = None
depart_delay = []

for line in sys.stdin:
    key, val = line.strip().split('\t')

    if last_key and last_key != key:
	if len(depart_delay) > 0:
            avg_delay = sum(depart_delay) / len(depart_delay)
	    print '%s\t%.3f' % (last_key, avg_delay)
        else:
	    print '%s\t%.3f' % (last_key,0)
	last_key = key
	if val != 'NA':
	    depart_delay = [float(val)]
	else:
	    depart_delay = []
    else:
        last_key = key
        if val != 'NA':
	    (month, day, time) = (x for x in key.split('_'))
	    depart_delay.append( float( val ) )

# Don't forget to print the last set
if last_key:
    if len(depart_delay) > 0:
        avg_delay = sum(depart_delay) / len(depart_delay)
        print '%s\t%.3f' % (last_key, avg_delay)
    else:
        print '%s\t%.3f' % (last_key,0)

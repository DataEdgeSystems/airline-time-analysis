#!/usr/bin/env python
"""
Reducer to bin the departure delay for flights departing from JFK

Emit (departure delay (mins), num trips with this departure delay)

@author Luigi Patruno
@date 28 Apr 2015
"""
import sys

last_key = None
num_trips = 0

for line in sys.stdin:
    key, val = line.strip().split('\t')

    if last_key and last_key != key:
        print '%s\t%s' % (last_key, num_trips)
        (last_key, num_trips) = (key, 1)
    else:
        (last_key, num_trips) = (key, num_trips+1)

# Don't forget to print the last set
if last_key:
    print '%s\t%s' % (last_key, num_trips)


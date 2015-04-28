#!/usr/bin/env python
"""
This is the reducer function to collect the number of flights departing from each airport

Emit (airportid, #incomingflights)

@author Luigi Patruno
@date 28 Apr 2015
"""
import sys

last_key = None
num_departing = 0

for line in sys.stdin:
    key, val = line.strip().split('\t')
    
    if last_key and last_key != key:
        print '%s\t%s' % (last_key, num_departing)
        (last_key, num_departing) = (key, 1)
    else:
        (last_key, num_departing) = (key, num_departing+1)

# Don't forget to print the last airport
if last_key:
    print '%s\t%s' % (last_key, num_departing)

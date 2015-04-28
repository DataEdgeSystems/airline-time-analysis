#!/usr/bin/env python
"""
Mapper to extract the arrival delay time for arriving at JFK

Emit (arrival delay (mins), 1)

@author Luigi Patruno
@date 28 Apr 2015
"""
import sys

for line in sys.stdin:
    info = line.strip().split(',')

    dest = info[17]
    
    if dest == 'JFK':
        if info[14] != 'NA':
            arrival_delay = int( info[14] ) 
            print '%d\t1' % arrival_delay
	else:
	    print 'NA\t1'

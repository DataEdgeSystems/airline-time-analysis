#!/usr/bin/env python
"""
Mapper to extract the depart delay time for trips departing from JFK

Emit (departure delay (mins), 1)

@author Luigi Patruno
@date 28 Apr 2015
"""
import sys

for line in sys.stdin:
    info = line.strip().split(',')

    origin = info[16]
    
    if origin == 'JFK':
        delay_time = info[15]
        if delay_time != 'NA':
            print '%d\t1' % int( delay_time )
	else:
	    print 'NA\t1'

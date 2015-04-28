#!/usr/bin/env python
"""
This python script filters the 2008 airport trip data to select all trips that were 
arriving at or departing from New York's JFK airport

@author Luigi Patruno
@date 28 Apr 2015
"""
import sys

JFK = 'JFK'

for line in sys.stdin:
    info = line.strip().split(',')

    origin = info[16].replace('"', '')
    dest = info[17].replace('"', '')

    if origin == JFK or dest == JFK:
        print '%s' % line.strip()    

#!/usr/bin/env python
"""
Mapper to extract the arrival delay time per trip arriving at JFK

Emit (originid_JFK, arrival delay time)

@author Luigi Patruno
@date 28 Apr 2015
"""
import sys

for line in sys.stdin:
    info = line.strip().split(',')

    origin = info[16]
    dest = info[17]

    if dest == 'JFK':
        key = '%s_%s' % (origin, dest)

        if info[14] != 'NA':
            arrival_delay = int( info[14] )
            print '%s\t%d' % (key, arrival_delay)
        else:
            print '%s\t%s' % (key, 'NA')


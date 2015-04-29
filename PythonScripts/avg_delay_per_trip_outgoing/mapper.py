#!/usr/bin/env python
"""
Mapper to extract the departure delay time per trips departing from at JFK

Emit (JFK_destid, departure delay time)

@author Luigi Patruno
@date 28 Apr 2015
"""
import sys

for line in sys.stdin:
    info = line.strip().split(',')

    origin = info[16]
    dest = info[17]

    if origin == 'JFK':
        key = '%s_%s' % (origin, dest)

        if info[15] != 'NA':
            departure_delay = int( info[15] )
            print '%s\t%d' % (key, departure_delay)
        else:
            print '%s\t%s' % (key, 'NA')


#!/usr/bin/env python
"""
This is the mapper function to collect the number of flights departing from each airport

If a trip is departing from an airport we print (airportid, +1)

@author Luigi Patruno
@date 28 Apr 2015
"""
import sys

for line in sys.stdin:
    info = line.strip().split(',')

    origin = info[16].replace('"', '')

    print '%s\t1' % origin

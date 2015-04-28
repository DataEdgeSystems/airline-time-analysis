#!/usr/bin/env python
"""
This is the mapper function to collect the number of flights arriving at each airport

If a trip is arriving at an airport we print (airportid, +1)

@author Luigi Patruno
@date 28 Apr 2015
"""
import sys

for line in sys.stdin:
    info = line.strip().split(',')

    #origin = info[16].replace('"', '')
    dest = info[17].replace('"', '')

    print '%s\t1' % dest

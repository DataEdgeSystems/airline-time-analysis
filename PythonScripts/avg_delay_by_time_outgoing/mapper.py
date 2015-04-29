#!/usr/bin/env python
"""
Mapper to extract the departure delay time by hour of day and day of year per trips departing from JFK

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
	month, day, depart_time, depart_delay = info[1], info[2], info[4], info[15]

	if depart_time != 'NA':
	    if len(depart_time) <= 2:
	        hour = depart_time
	        minute = 0
	    elif len(depart_time) == 3:
		hour = depart_time[:1]
		minute = depart_time[1:]
	    else: 
	        hour = depart_time[:2]
	        minute = depart_time[2:]
	    # Bin every 30 minutes
	    if minute < 30:
		key = '%s_%s_%s00' % (month, day, hour)
	    else:
		key = '%s_%s_%s30' % (month, day, hour)

            print '%s\t%s' % (key, depart_delay)


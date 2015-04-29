#!/usr/bin/env python
"""
Get the map data necessary for visualization showing worst flights from JFK by avg departure delay

@author Luigi Patruno
@date 28 Apr 2015
"""
import pandas as pd
import csv

file_path = '../../data/avg_delay_per_trip_outgoing/part-00000'

departs = []
avg_depart_delay = []
num_trips = []

f = open(file_path)

for line in f:
    key, val = line.strip().split('\t')
    departs.append( key.split('_')[1] )
    avg_depart_delay.append( float( val.split('_')[0] ) )
    num_trips.append(( int( val.split('_')[1] ) ))

f.close() 


# Get the latitude and longitude points for each of the airports
lats = []
lons = []
airports = '../../data/raw/airports.csv'

with open(airports) as csvfile:
    reader = csv.reader(csvfile)
    for id in departs:
        for row in reader:
            if row[0] == id:
                lats.append( float(row[5]) )
		lons.append( float(row[6]) )	
		break


df = pd.DataFrame({'departs': departs, \
		   'avg_depart_delay': avg_depart_delay, \
		   'num_trips': num_trips, \
		   'latitude': lats, \
		   'longitude': lons})

df['total_delay'] = df['avg_depart_delay'] * df['num_trips']
df = df.sort('total_delay', ascending = False)

for i in range(15):
    name = df.iloc[i]['departs']
    lat = df.iloc[i]['latitude']
    lon = df.iloc[i]['longitude']
    delay = df.iloc[i]['avg_depart_delay']
    trips = df.iloc[i]['num_trips']
    print "{name:'%s', delay:%.3f, trips:%d, lat:%f, lon:%f}," % (name, delay, trips, lat, lon) 

print

for i in range(15):
    name = df.iloc[i]['departs']
    lat = df.iloc[i]['latitude']
    lon = df.iloc[i]['longitude']
    delay = df.iloc[i]['avg_depart_delay']
    print "{name:'%s', z:%.3f, lat:%f, lon:%f}," % (name, 10*delay, lat, lon)






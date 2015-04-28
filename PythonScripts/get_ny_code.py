"""
This script is to extract the airport code for JFK airport

The script prints out all rows from the airports.csv file where the city is 'New York'

@author Luigi Patruno
@date 28 Apr 2015
"""
import csv

# relative path to file
airports = '../data/airports.csv'

with open(airports) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[2] == 'New York':
            print row


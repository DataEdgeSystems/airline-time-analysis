#!/bin/bash

# Using hadoop-streaming API to filter the flight data for flights
# arriving to and departing from JFK

# remove the existing output directory in HDFS 
hadoop fs -rm -r fp_data/ny_flights

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
	-input  fp_data/raw/2008.csv \
	-output fp_data/ny_flights \
	-file '../PythonScripts/filter_ny/mapper.py'  -mapper 'python mapper.py' \
	-file '../PythonScripts/filter_ny/reducer.py' -reducer 'python reducer.py'

hadoop fs -copyToLocal fp_data/ny_flights/ ../data/



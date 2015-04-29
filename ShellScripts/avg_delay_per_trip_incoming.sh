#!/bin/bash

# Using hadoop-streaming API to get the average arrival delay per trip for flights arriving at JFK

# remove the existing output directory in HDFS 
hadoop fs -rm -r fp_data/avg_delay_per_trip_incoming

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
        -input  fp_data/ny_flights/part-00000 \
        -output fp_data/avg_delay_per_trip_incoming \
        -file '../PythonScripts/avg_delay_per_trip_incoming/mapper.py'  -mapper 'python mapper.py' \
        -file '../PythonScripts/avg_delay_per_trip_incoming/reducer.py' -reducer 'python reducer.py'

hadoop fs -copyToLocal fp_data/avg_delay_per_trip_incoming ../data/

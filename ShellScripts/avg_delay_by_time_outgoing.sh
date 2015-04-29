#!/bin/bash

# Using hadoop-streaming API to get the average departure delay by time for flights departing from JFK

# remove the existing output directory in HDFS 
hadoop fs -rm -r fp_data/avg_delay_by_time_outgoing

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
        -input  fp_data/ny_flights/part-00000 \
        -output fp_data/avg_delay_by_time_outgoing \
        -file '../PythonScripts/avg_delay_by_time_outgoing/mapper.py'  -mapper 'python mapper.py' \
        -file '../PythonScripts/avg_delay_by_time_outgoing/reducer.py' -reducer 'python reducer.py'

hadoop fs -copyToLocal fp_data/avg_delay_by_time_outgoing ../data/

#!/bin/bash

# Using hadoop-streaming API to get the bins for departure delay for flights departing from JFK

# remove the existing output directory in HDFS 
hadoop fs -rm -r fp_data/delay_bins_outgoing

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
        -input  fp_data/ny_flights/part-00000 \
        -output fp_data/delay_bins_outgoing \
        -file '../PythonScripts/delay_bins_outgoing/mapper.py'  -mapper 'python mapper.py' \
        -file '../PythonScripts/delay_bins_outgoing/reducer.py' -reducer 'python reducer.py'

hadoop fs -copyToLocal fp_data/delay_bins_outgoing ../data/

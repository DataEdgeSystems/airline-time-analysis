#!/bin/bash

# Using hadoop-streaming API to get the number of incoming flights for each airport

# remove the existing output directory in HDFS 
hadoop fs -rm -r fp_data/num_incoming_by_airport

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
        -input  fp_data/raw/2008.csv \
        -output fp_data/num_incoming_by_airport \
        -file '../PythonScripts/num_incoming_by_airport/mapper.py'  -mapper 'python mapper.py' \
        -file '../PythonScripts/num_incoming_by_airport/reducer.py' -reducer 'python reducer.py'

hadoop fs -copyToLocal fp_data/num_incoming_by_airport ../data/

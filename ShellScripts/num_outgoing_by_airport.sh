#!/bin/bash

# Using hadoop-streaming API to get the number of departing flights for each airport

# remove the existing output directory in HDFS 
hadoop fs -rm -r fp_data/num_outgoing_by_airport

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
        -input  fp_data/raw/2008.csv \
        -output fp_data/num_outgoing_by_airport \
        -file '../PythonScripts/num_outgoing_by_airport/mapper.py'  -mapper 'python mapper.py' \
        -file '../PythonScripts/num_outgoing_by_airport/reducer.py' -reducer 'python reducer.py'

hadoop fs -copyToLocal fp_data/num_outgoing_by_airport ../data/

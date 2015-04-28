#!/bin/bash

# Shell script to extract the 20 airports with the most incoming flights and 20 airports with most departing flights

cat ../data/num_outgoing_by_airport/part-00000 | sort -k2 -n -r | head -20 > ../data/num_outgoing_by_airport/top_20_outgoing

cat ../data/num_incoming_by_airport/part-00000 | sort -k2 -n -r | head -20 > ../data/num_incoming_by_airport/top_20_incoming

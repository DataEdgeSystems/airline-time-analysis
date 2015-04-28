#!/usr/bin/env python
"""
This script generates the histogram for the delayed incoming JFK flights

@author Luigi Patruno
@date 28 Apr 2015
"""
import numpy as np
import pandas as pd
import matplotlib


def main():
    # Disable display
    matplotlib.use('Agg')

    import matplotlib.pyplot as plt

    file_path = '../../data/delay_bins_incoming/part-00000'

    # DataFrame object containing the top 20 airports with most incoming flights
    df = pd.read_csv(file_path, sep='\t', header=None)
    df = df.sort(0)

    bins = {}
    x_labels = []
    y = []

    for i in range( df.shape[0] ):
        try:
            delay = int( df.iloc[i][0] )
            if delay < 0:
                delay = abs( delay )	    
	        mod = delay % 30
	        key = (int( (delay - mod) / 30 ) * -1) - 1 #Excuse this stupid additive factor
            else:
                mod = delay % 30
                key = int( (delay - mod) / 30 )
	        #key = '%d_%d' % (quotient*30, (quotient*30)+30)
	    if key in bins:
	        bins[key] += int( df.iloc[i][1] )
	    else:
	        bins[key] = int( df.iloc[i][1] )
        except:
	    pass

    for k in sorted(bins.keys()):
        label = '%d_%d' % (k*30, k * 30 + 30)
	x_labels.append( label )
        y.append( bins[k] )


    x = np.arange( len(y) )


    fig, ax = plt.subplots()

    fig.set_size_inches(10,6)

    plt.title('Arrival Delays for Incoming Flights')
    
    plt.xticks( x + .25, x_labels, rotation=75)
    plt.xlim([min(x) - .5, max(x) + 1])

    # Hide the right and top spines
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_color('gray') 
    ax.spines['bottom'].set_color('gray') 
    
    # Hide tick marks
    ax.yaxis.set_ticks_position('none')
    ax.xaxis.set_ticks_position('none')

    plt.bar(x, y, width=.5, color='maroon', edgecolor='none')
    plt.savefig("../../plots/histogram_incoming_delays.png")


if __name__ == '__main__':
    main()



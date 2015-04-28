#!/usr/bin/env python
"""
This script generates the bar plot for the top 20 airports with the most outgoing flights

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

    file_path = '../../data/num_outgoing_by_airport/top_20_outgoing'

    # DataFrame object containing the top 20 airports with most outgoing flights
    df = pd.read_csv(file_path, sep='\t', header=None)

    x = np.arange(20)
    x_labels = df[0].values
    y = df[1].values

    fig, ax = plt.subplots()

    fig.set_size_inches(10,6)

    plt.title('Top 20 Airports by Number of Outgoing Flights')
    
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

    plt.savefig("../../plots/top_20_outgoing.png")

if __name__ == '__main__':
    main()



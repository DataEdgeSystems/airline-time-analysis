#!/usr/bin/env python
"""
This script generates the bar plot for the top 20 airports with the most incoming flights

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

    file_path = '../../data/num_incoming_by_airport/top_20_incoming'

    # DataFrame object containing the top 20 airports with most incoming flights
    df = pd.read_csv(file_path, sep='\t', header=None)

    x = np.arange(20)
    x_labels = df[0].values
    y = df[1].values

    plt.bar(x, y)
    plt.savefig("../../plots/top_20_incoming.png")

if __name__ == '__main__':
    main()



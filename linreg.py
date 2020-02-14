#!/usr/bin/env python3

import csv
import sys

def read_data(filename):
    x = []
    t = []
    with open(filename) as csvfile:
        data = csv.reader(csvfile)
        for year, time in data:
            x.append(float(year))
            t.append(float(time))
    return x, t

def average(array):
    return sum(array) / len(array)

# Try this with both data.txt and olympic100m.txt.

x, t = read_data(sys.argv[1])

# TODO: Replace '?'s with code to compute the desired value.

x_bar = '?'
t_bar = '?'
xt_bar = '?'

w0_hat = '?'
w1_hat = '?'

print(f'y = {w0_hat} + {w1_hat}x')

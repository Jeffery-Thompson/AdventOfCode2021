#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# advent of code day 1, problem 1 & 2
import numpy as np
depths = np.loadtxt('./data/day1.txt')

# prob 1
diff = np.diff(depths, n=1)
increase = diff >0
print('number of increases: {}'.format(sum(increase)))

# prob 2
window = np.convolve(depths, np.ones(3,dtype=int), 'valid')
diffs = np.diff(window)
increase = diffs > 0
print('number of increases, with window: {}'.format(sum(increase)))
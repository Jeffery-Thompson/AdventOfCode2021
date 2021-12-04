#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# advent of code day 3, problem 1 & 2

# import pandas as pd
import numpy as np
from numpy.core.numeric import binary_repr
from numpy.lib.shape_base import column_stack
from scipy import stats
from scipy.stats.stats import ModeResult

test = np.asarray(['00100', '11110','10110', '10111',
        '10101', '01111', '00111', '11100',
        '10000', '11001', '00010', '01010'], dtype='str')

def binary_to_decimal(array):
    '''Convert np array of 0,1s to '''
        # from stack overflow :/ 
    return (array.dot(2**np.arange(array.size)[::-1]) )

def submarine_power(data):
    '''Function to calculate subs power'''
    #  courtesy of EarthLab's Nathan Korinek
    data = [np.fromiter(binary, dtype=int) for binary in data]

    gamma = stats.mode(data)[0].flatten()
    epsilon = (~gamma.astype('bool')).astype('int')

    # from stack exhange :/
    gamma = binary_to_decimal(gamma)
    epsilon = binary_to_decimal(epsilon)

    return (gamma * epsilon)

data = list(np.loadtxt('./data/day03.txt', str))

power = submarine_power(data)

print('power is: {}'.format(power))

# part b
def binary_to_int_array(data):
    '''Converts binary stings to array of numpy ints '''
    data = [np.fromiter(binary, dtype=int) for binary in data]
    
    return (np.asarray(data))


def get_binary_mode(slice, invert = False, small=True):
    '''Function to find most and least common bit from numpy array'''
    
    mode, count = stats.mode(slice)
    mode = mode.flatten()
    
    if invert and (slice.shape[0] % count) != 0:
        mode = (~mode.astype('bool')).astype('int')
    # elif invert and (slice.shape[0] % count) == 0:
    
    # by default, mode returns smallest in case of ties
    #  to return largest in case of ties
    if not small and (slice.shape[0] % count) == 0:
        mode = (~mode.astype('bool')).astype('int')

    return(mode)

def subset_array(array, value, col):
    '''Subset an array by value in a specific column '''
    idx = array[:,col] == value
    
    return(array[idx,:])

def filter_array(array, **kwargs):
    '''Filter 2D array using column mode values'''
    subset = array.copy()
    for col in range(array.shape[1]):
        
        mode = get_binary_mode(subset[:,col], **kwargs)
        # print(mode)
        subset = subset_array(subset, mode, col)
        # print(subset)

    return subset

data = binary_to_int_array(list(np.loadtxt('./data/day03.txt', str)))

oxygen = filter_array(data, small=False)
co2 = filter_array(data, invert=True)


print('life support is: {}'.format(binary_to_decimal(oxygen) * binary_to_decimal(co2)))
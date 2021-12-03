#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# advent of code day 3, problem 1 & 2

# import pandas as pd
import numpy as np
from numpy.lib.shape_base import column_stack
from scipy import stats

test = np.asarray(['00100', '11110','10110', '10111',
        '10101', '01111', '00111', '11100',
        '10000', '11001', '00010', '01010'], dtype='str')

def word_to_ints(word):
    '''Split a word into letters'''
    word = list(word)
    int_list = [int(c) for c in word]
    return(int_list)

def array_to_decimal(array):
    '''Convert np array of 0,1s to '''
        # from stack overflow :/ 
    return (array.dot(2**np.arange(array.size)[::-1]) )

def submarine_power(data):
    '''Function to calculate subs power'''
    data = [word_to_ints(d) for d in data]

    gamma = stats.mode(data)[0].flatten()
    epsilon = (~gamma.astype('bool')).astype('int')

    # from stack exhange :/
    gamma = array_to_decimal(gamma)
    epsilon = array_to_decimal(epsilon)

    return (gamma * epsilon)

data = list(np.loadtxt('./data/day03.txt', str))

power = submarine_power(data)

print('power is: {}'.format(power))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# advent of code day 2, problem 1 & 2

import pandas as pd
import numpy as np

data = pd.read_csv('./data/day02.txt', sep =' ', names=['direction', 'unit'])

# problem 1
x = 0
y = 0

x += data[data.direction=='forward']['unit'].sum()
y += (data[data.direction =='down']['unit'].sum() - data[data.direction =='up']['unit'].sum())

print('total movement (x * y): {} '.format(x*y))

# problem 2
aim = 0; hor = 0; depth = 0

for i,r in data.iterrows():
     if r.direction=='down' :
         aim += r.unit
     elif r.direction=='up' :
         aim += -r.unit
     else :
         hor += r.unit
         depth += r.unit * aim

print('total movement (hor * depth): {} '.format(hor * depth))
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 11:11:51 2020

@author: Pranav Devarinti
"""

import numpy as np

def isprime(x):
    return False if (x % np.arange(2,(x/2)+1,1) == 0).any() else True

def prime_generator(start,stop):
    return np.arange(start,stop)[[isprime(i) for i in range(start,stop)]]


def is_prime(x):
    rt = True
    for i in range(2,x):
        if x % i == 0:
            rt = False
    return rt

#Prime Generator
# Generates a list of prime from start to stop

a = [1,2,3,4]
b = [2,2,3,4]

c = [sum(i) for i in zip(a,b)]


def s_s_prime_generator(start,stop):
    return np.arange(start,stop)[[(False if (i % np.arange(2,(i/2)+1,1) == 0).any() else True) for i in range(start,stop)]]


def list_sort(a:list) -> list:
    # return a ordered from greatest to least
    # You cannot use list.sort()
    out = []
    while True:
        l_max = a[0]
        l_max_index = 0
        for index,value in enumerate(a):
            if l_max < value:
                l_max_index = index
        out.append(a.pop(l_max_index))
        if len(a) == 0:
            break
    return out


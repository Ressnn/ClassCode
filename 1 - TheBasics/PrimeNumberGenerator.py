# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 10:32:48 2020

@author: Pranav Devarinti
"""
# Lets make a prime number generator!

# In[] Define relevant variables

start = 2;
stop = 10;

# In[] Function to tell if one number is divisible by another

def divisible(a :int,b :int) -> bool:
    return a%b==0 

# In[] IsPrime function

def IsPrime(x :int) -> bool:
    IsNotPrime = False 
    for divisor in range(2,x):
        IsNotPrime = IsNotPrime or divisible(x,divisor)
    return not(IsNotPrime)
        
# In[] Loop is prime over the start and stop

def generatePrimes(start :int, stop :int) -> list:
    myList = []
    for i in range(start,stop):
        if IsPrime(i):
            myList.append(i)
    return myList

A = generatePrimes(2,10000)



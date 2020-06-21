# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 11:38:21 2020

@author: Pranav Devarinti
"""
"""

if boolean:
    logic
else:
   logic 
    
"""
"""
if (True):
    print("It is true")
else:
    print("It is false")
"""
# In[]
if True:
    print("A")
else:
    print("B")
# In[]

if False:
    print("A")
else:
    if True:
        print("C")
    else:
        print("B")

# In[]
   
"""
conditions
== equal to
> greater than
< less than
>= greater than or equal to
<= less than or equal to
"""
# In[]
a = 0
b = 1

# In[]
if a==b:
    print("A==B")
else:
    print("A is not equal to B")
# In[]











# In[]
"""
condition modifiers
and - returns true if a and b are true
not - takes the opposite of an input
or - returns true if a or b is true 
^(xor) - exclusive or
"""

a =True
b =False

not(b)

a and b
a or b

"""
Functions and if statements
"""



"""
Practice:
#1:
A game has a currency system
write a function to check if a the currency owned
is more than the currency that the player has 

Given: PlayerBalance , ItemCost
Expected_output: boolean representing if the item can be bought

def afford(PlayerBalance,ItemCost):
    if PlayerBalance>=ItemCost:
        return True
    else:
        return False




#2:
A manufacturer has specifications on a tire
the diameter must be withing 1cm of the specifications
write a function to compare if a given tire meets the specifications

Given: Spec_diameter, diameter
Expected_output: if the tire meets the criteria

"""
# In[]

def MeetsSpecs(Spec_Diameter,diameter):
    minimum = Spec_Diameter-1
    maximum = Spec_Diameter+1
    if diameter>minimum:
        if diameter<maximum:
            return True
    return False



a=0
b=0

if not(a==b):
    print("True")
else:
    print("False")


# In[]

import math

import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = plt.axes(projection="3d")

def isWitihin1(a,b,EPSILON):
    if(a-b <=EPSILON):
        if(a-b >=-EPSILON):
            return True
    return False


def isWitihin(a,b,EPSILON):
    if(abs(a-b) <=EPSILON):
        return True
    return False

# In[]

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random

def func(a,b,EPSILON):
    if(abs(a-b) <=EPSILON):
        return True
    return False

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
n = 30
xs = [i for i in range(n) for _ in range(n)]
ys = list(range(n)) * n
zs = [func(x, y,5) for x,y in zip(xs,ys)]

ax.scatter(xs, ys, zs)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()







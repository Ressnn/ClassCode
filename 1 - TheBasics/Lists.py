# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 10:55:14 2020

@author: Pranav Devarinti
"""


"""
Lists are lists of variables of other types
there are two ways to define a list"""

myList = list()
myList = []

# In[]
""" 
There are two ways to add values to a list
"""
myList.append("MyName:")
# In[]
myList += ["Pranav","Devarinti"]

print(myList)
# In[]
"""
StringName.split("valuetosplitby")
"""


myList = []
myList += "Pranav,Reddy,Devarinti".split(",")
# In[]
"""
To get items from a list do it like so
list_name[index]

Remember Indecies start at 0
"""

print(myList[-1])


# In[]
"""
To get multiple items from a list do it like so
list_name[start:stop:step]
"""
myList = [1,2,3,4,5,6,7,8]

#get me the first 3 values
print(myList[4:-1])


#write me a function that will take
# a string as an input and reverse it


# In[]


#Can you print out 2 5 and 8
print(myList[1::3])

# In[]
"""
Numpy arrays
"""
import numpy as np
myArray = np.array([1,2,3,4,5])
print(myArray)

"""
Numpy array to a list
"""
print(myArray.tolist())











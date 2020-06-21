# -*- coding: utf-8 -*-
"""
Created on Sun May 17 10:48:35 2020

@author: Pranav Devarinti
"""

"""
While Loops

while (condition):
    code

"""


# In[]
x = 0
while x<1000:
    x+=1
    print(x)
    
# In[]

#Print out overy odd number from 1 ->1000

counter = 1
while counter<=1000:
    if counter%2 == 1:
        print(counter)
    counter +=1
# In[]
# print out every integer from 1 to 100
counter =1
while counter<=100:
    print(counter)
    counter += 1
# In[]
"""
For Loops:

for value in values:
    do something


for value in range(start,stop):
    do something
    
"""
myList = ["Item1","Item2","Item3"]
for item in myList:
    print(item)
# In[]
for index in range(0,10):
    print(index)
# In[]







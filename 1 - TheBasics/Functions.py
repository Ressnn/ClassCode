"""
Making a function in python can be broken up into parts:

first we use the key-word def to tell python
that we are defining a new function
Then, we type the function name and an open parenthesis
Then, we type inputs seperated by commas
Finally, we type a closing bracket and semicolon that will tell python
that the indented code is part of a function.

If the function should return something then add a return statement
and the variable to return

Putting it all together, it should look something like this:
"""
#Sample Function to take the average of two inputs
def average(input_a,input_b):
    #insert logic here
    output = (input_a+input_b)/2
    # Return statement (optional)
    return output
import math
def sqrt(x):
    return math.sqrt(x)

def circ(radius):
    output = 2*3.14*radius
    return output

def areaOfCircle(radius):
    return 3.14*radius**2

# One box inside another
# How much volume is left
# l1 w1 h1 l2 w2 h2 given
# return the volume left

def boxvol(a :int,b :int,c :int):
    avol = a*b*c
    return avol

def b1minusb2(l1,l2,w1,w2,h1,h2):
    return boxvol(l1,w1,h1)-boxvol(l2,w2,h2)



#Make a function to compute the volume of a cube
# given the side-length
#
#Call the function for a side_length of 6 
#and print the output with a m^3 attached to the 
# end

def volume(side_length):
    return side_length**3

volume6 = volume(6)
print(str(volume6)+" m^3")

"""
Now that we have made a function with some logic, we can take it and
call it on some inputs like so: function_name(inputs)
"""

numaverage = average(1,2)
average(1,2)

# In[]




























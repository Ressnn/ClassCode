#!/usr/bin/env python
# coding: utf-8

# # All About Classes

# ### Objects and Classes

# 1. Everything physical can be represented as the sum of objects.
# 2. Objects Store information in themselves (As their state)
# 3. Most Objects can be generalized

# Before we delve into any actual programming imagine pick any real world object around you. It stores information (color, shape, ect.) in it's state and is also likley made up of other sub-objects. If you know what to call it then that means that it also can be generalized into a greater class.
# 
# You -> Human -> Object
# Dog -> Animal -> Object
# Alien -> Organism -> Object
# Meteor -> Spatial Bodies -> Object
# 
# We can also go the other way (which is how objects are usually created)
# 
# Human -> You 
# Animal -> Dog
# Organism -> Alien
# Spatial Bodies -> Meteor

# ### basic class that does nothing and stores nothing

# In[46]:


class Basic():
    pass


# Defining a class is a lot like defining a function you type in class [classname](inhertedobjects):  to start a class past the indent

# ### Functions and Classes

# In[24]:


class Dog():
    def bark():
        return "barking"
    def Isscared():
        return False


# We can put functions inside of classes to give the objects created from these classes things to do. The resulting dog object in this case can bark

# ### The __init__ function

# In[51]:


class Dog():
    def __init__(self,fur_color,age):
        self.fur_color = fur_color
        self.age = age
    def bark(self):
        return "barking"
    def scared(self):
        return False
    def eat(self):
        return 20-self.age


# By using the __init__ function we can store properties about the dog inside of it when it is created
# 
# In the example above we store the age and the fur_color

# ## Making an Object

# In the code above we defined how to make a dog, but never actually made one to actually make one you have to run the line below

# In[52]:


myDog = Dog("orange",4)


# In[53]:


myDog.eat()


# ### Excercise 1

# Make me a new class called car give it number of wheels (in the init function) and add a drive function

# In[54]:


class Car():
    def __init__(self,wheels):
        self.wheels = wheels
    def drive(self):
        return "Driving"


# ### Excercise 2

# Make a class called employee with an age and a height and travel distance

# In[60]:


class Employee():
    def __init__(self,age, height, travel):
        self.age = age
        self.height = height
        self.travel = travel


# Now Make a company class where I specify the number of Employees by giving a list of charechteristics. Plug this into a Company class with a list of the generated employees.

# In[61]:


employee_List = [[21,70,1],[17,71,10],[23,60,10]]

class Company():
    def __init__(self,employee_features):
        self.employees = []
        for prospecting_employee in employee_features:
            age = prospecting_employee[0]
            height = prospecting_employee[1]
            travel = prospecting_employee[2]
            self.employees.append(Employee(age,height,travel))
            
Ls = Company(employee_List)
Ls.employees


# In[ ]:





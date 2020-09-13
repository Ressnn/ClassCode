# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 10:59:49 2020

@author: Pranav Devarinti
"""


import numpy as np


x_pct = .1
population = 1000
infection_rate = .8
kill_chance_malaria = .2
sickle_cell = .42
people = np.random.choice([1,0],p=[x_pct,1-x_pct],size=(population,2))

def malaria_infect(people):
    for index,value in enumerate(people):
        if (value == np.array([0,0])).all():
            if np.random.choice([True,False],p=[infection_rate*kill_chance_malaria,1-infection_rate*kill_chance_malaria]):
                people[index] = np.array([2,2])

def sickle_kill(people):
    for index,value in enumerate(people):
        if (value == np.array([1,1])).all():
            if np.random.choice([True,False],p=[sickle_cell,1-sickle_cell]):
                people[index] = np.array([2,2])

def repopulate(people):
    dead = people == 2
    dead = dead[:,0]
    alive = people[dead == False]
    
    for index,value in enumerate(dead):
        if value != True:
            gene_pool = np.random.choice(alive,size=2).reshape(-1)
            new_genes = np.random.choice(gene_pool,size=2)
            dead[index,:] = new_genes
                    
    
for i in range(0,100):
    malaria_infect(people)            
    sickle_kill(people)
    repopulate(people)
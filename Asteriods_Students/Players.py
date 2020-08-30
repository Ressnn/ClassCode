import pygame
import numpy as np
import os
import random

class Ship(pygame.sprite.Sprite):
    def __init__(self,width,height):
        pygame.sprite.Sprite.__init__(self)
        
        self.original_image = pygame.image.load("Assets/Ship.png")
        self.image = self.original_image.copy()
        
        self.rect = self.image.get_rect()
        self.momentum = np.zeros(2,)
        self.angle = 0
    
        self.rect.center = (width/2,height/2)
        self.subcenter = self.rect.center

    def rotate(self,angle):
        self.angle += angle
        self.image = pygame.transform.rotate(self.original_image,self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        
    def thrust(self,power):
        rad_angle = -1*np.deg2rad(self.angle+90)
        self.momentum += np.array([np.cos(rad_angle)*power,np.sin(rad_angle)*power])

    def update(self):
        print(self.subcenter)
        self.subcenter += self.momentum
        self.momentum = self.momentum/1.01
        self.rect.center = self.subcenter
        
class Asteroid(pygame.sprite.Sprite):
    def __init__(self,width,height,buffer=20,buffer2=50):
        pygame.sprite.Sprite.__init__(self)
        
        paths = [os.path.join("Assets/Asteriods",i) for 
                 i in os.listdir("Assets/Asteriods")]
        
        img_path = random.choice(paths)
        
        self.w = width
        self.h = height
        self.buffer = buffer
        self.buffer2 = buffer2
        self.rot = np.random.randint(0,180)
        self.momentum = np.random.normal(size=(2,))
        self.spin_momentum = np.random.normal()
        
        self.original_image = pygame.image.load(img_path)
        self.image = pygame.transform.rotate(self.original_image,self.rot)
        
        self.rect = self.image.get_rect(center=self.get_spawn_point())
        
    def get_spawn_point(self):
        return self.generate_x(),self.generate_y()
        
    def generate_x(self):
        point = np.random.uniform(-self.buffer,self.buffer)
        if point > 0:
            point += self.w
        return point
    
    def generate_y(self):
        point = np.random.uniform(-self.buffer,self.buffer)
        if point > 0:
            point += self.h
        return point
    
    def update(self):
        self.rect.x += self.momentum[0]
        self.rect.y += self.momentum[1]
        self.rot += self.spin_momentum
        self.image = pygame.transform.rotate(self.original_image,self.rot)
        self.rect = self.image.get_rect(center=self.rect.center)
        
        location = np.array([self.rect.x,self.rect.y])
        if (location< -np.array([0,0])-self.buffer2).any() or \
        (location>np.array([self.w,self.h])+self.buffer2).any():
            self.kill()
        
    
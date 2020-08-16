import pygame
import numpy as np


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
        self.momentum += np.array([np.cos(self.angle+90)*power,np.sin(self.angle+90)*power])
 
    def update(self):
        self.subcenter += self.momentum
        self.momentum = self.momentum/1.01
        self.rect.center = self.subcenter
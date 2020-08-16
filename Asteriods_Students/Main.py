import pygame as pg
from pygame.locals import QUIT

import numpy as np

import Players

class AsteroidsGame():
    def __init__(self,size=(800,600)):
        self.dims = np.array(size)
        
        pg.init()
        self.screen = pg.display.set_mode(self.dims)
        pg.display.set_caption("Asteroids")
        
        self.initialize()
        while not(self.game_loop()):
            pass
    
    def check_quit(self,event):
        if event.type == QUIT:
            print("Quitting")
            return True
        return False
    
    def initialize(self):
        self.global_group = pg.sprite.Group()
        self.player_sprite = Players.Ship(self.dims[0],self.dims[1])
        self.global_group.add(self.player_sprite)
    
        
    
    def draw(self):
        background = pg.Surface(self.dims)
        background.fill((9,50,25))
        self.screen.blit(background,(0,0))        
        self.global_group.draw(self.screen)
        
    def ship_movement(self):
        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP]:
            self.player_sprite.thrust(0.01)
        if key_states[pg.K_DOWN]:
            self.player_sprite.thrust(-0.01)
        if key_states[pg.K_LEFT]:
            self.player_sprite.rotate(-1)
        if key_states[pg.K_RIGHT]:
            self.player_sprite.rotate(1)
    def game_loop(self):
        leave_game = False
        
        self.ship_movement()
        self.global_group.update()
        self.draw()
        
        pg.display.flip()
        
        for event in pg.event.get():
            if self.check_quit(event):
                pg.quit()
                leave_game = True
                break
        return leave_game
    
    
        
A = AsteroidsGame()
        
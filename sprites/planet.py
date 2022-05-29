from curses import window
from re import X
import pygame
import math

from sprites.astronaut import Player

class Planet(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.circle = pygame.draw.circle(window, (0,0,0) , (x,y), 100 ) #Will continue and fix tomorrow
        self.active = (self.circle).collideract(Player)
        
        self.x = x
        self.y = y
        
        self.height = 200
        self.width = 200
        
    def render(self,game):
        
        planet = pygame.transform.scale(self.image,(self.width, self.height))
        gravity = pygame.transform.scale(self.circle,(self.width*2,self.height*2))
        
        #game.window.blit(planet, (self.x, self.y))
        game.window.blit(gravity, (self.x, self.y)) 
        self.update(game)
        
        return {
            'state': game.data,
            'run': True
        }
    
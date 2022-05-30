import pygame
import math

class Planet(pygame.sprite.Sprite):
    def __init__(self,planet_type,x,y,game):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(planet_type)
        
        self.x = x
        self.y = y
        
        self.height = 200
        self.width = 200
        
    def render(self,game):
        
        planet = pygame.transform.scale(self.image,(self.width, self.height))
        
        game.window.blit(planet, (self.x, self.y))
        self.update(game)
        
        return {
            'state': game.data,
            'run': True
        }
    
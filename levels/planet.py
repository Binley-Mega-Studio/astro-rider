import pygame
import math

class Gravity(pygame.sprite.Sprite):
    def __init__(self,x,y,game):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load("levels/planets/Gravity.png")
        self.image.set_alpha(64)
        self.height = 400
        self.width = 400
        self.x = x
        self.y = y
    def render(self,game):
        gravity = pygame.transform.scale(self.image,(self.width, self.height))
        game.window.blit(gravity, (self.x-100, self.y-100))

      
class Planet(pygame.sprite.Sprite):
    def __init__(self,planet_type,x,y,game):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load("levels/planets/"+planet_type)
        self.x = x
        self.y = y
        self.gravity = Gravity(self.x,self.y,game)
        self.height = 200
        self.width = 200
        
    def render(self,game):
        
        planet = pygame.transform.scale(self.image,(self.width, self.height))
        self.gravity.render(game)
        game.window.blit(planet, (self.x, self.y))
        
        return {
            'state': game.data,
            'run': True
        }
    
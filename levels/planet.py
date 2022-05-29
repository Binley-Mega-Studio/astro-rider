import pygame
import math

class Planet(pygame.sprite.Sprite):
    
    def __init__(self,image,x,y,game,player):
        
        self.player = player
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.circle = pygame.draw.circle(game.window, (0,0,0) , (x,y), 100 ) #Will continue and fix tomorrow
        
        self.x = x
        self.y = y
        
        self.height = 200
        self.width = 200
        
    def render(self,game):
        
        planet = pygame.transform.scale(self.image,(self.width, self.height))
        gravity = pygame.transform.scale(self.circle,(self.width*2,self.height*2))
        
        game.window.blit(planet, (self.x, self.y))
        game.window.blit(gravity, (self.x, self.y)) 
        self.update(game)
        
        return {
            'state': game.data,
            'run': True
        }
    
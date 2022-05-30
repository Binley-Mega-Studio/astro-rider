from pygame.locals import *
from levels import *
from levels import level
from sprites import astronaut
import pygame

class Play:
    '''
    Actual gameplay
    Contents: (Actual gameplay)
    '''
    def __init__(self,game):
        self.state = 1
        self.player = astronaut.Player()
        self.level = level.Level(game)
        self.level.load_level(game)
        self.backdrop = pygame.image.load('Backdrop.png')
        
    def render(self, game):
        game.window.fill((0, 0, 0))
        game.window.blit(self.backdrop, (0,0))
        self.level.render(game) 
        #self.planet_data = self.planet.render(game)
        
        self.player_data = self.player.render(game, self)
    

        return {
            'state': self.state,
            'run': True
        }

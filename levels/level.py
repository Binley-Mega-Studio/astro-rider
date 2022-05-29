import pygame
from pygame.locals import *


class Level:
    '''
    Actual gameplay
    Contents: (Actual gameplay)
    '''
    def __init__(self):
        pass
    def render(self, game):
        
        game.window.fill((0, 0, 0))
        
        #self.planet_data = self.planet.render(game)
        
        self.player_data = self.player.render(game, self)
        

        return {
            'state': self.state,
            'run': True
        }

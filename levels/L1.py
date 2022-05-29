import pygame
from pygame.locals import *


class L1:
    '''
    Kill me
    '''
    def __init__(self):
        self.planets = []
        self.planet_type = 'Planet_1'
        self.music = 'Music_1'
        self.backdrop = 'Backdrop_1'
        
    def render(self, game):
        
        game.window.fill((0, 0, 0))
        
        #self.planet_data = self.planet.render(game)
        
        self.player_data = self.player.render(game, self)
        

        return {
            'state': self.state,
            'run': True
        }

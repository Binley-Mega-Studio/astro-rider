import pygame
from pygame.locals import *
from sprites import astronaut


class Play:
    '''
    Actual gameplay
    Contents: (Actual gameplay)
    '''
    def __init__(self):
        self.state = 1
        self.player = astronaut.Player()
        
    def render(self, game):
        
        game.window.fill((48, 48, 48))
        
        self.player.render(game)
        

        return {
            'state': self.state,
            'run': True
        }

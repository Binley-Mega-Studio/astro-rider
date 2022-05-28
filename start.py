import pygame
from pygame.locals import *

class Start:
    '''
    Start menu / title screen
    Contents: (Play button, settings, level select, exit game)
    '''
    def __init__(self):
        self.status = 0
        
    def render(self, game):
        game.window.fill((255,0,0))
        
        return {
            'state': self.status,
            'run': True
        }
        

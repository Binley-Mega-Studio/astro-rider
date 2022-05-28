import pygame
from pygame.locals import *

class Pause:
    '''
    Pause menu
    Contents: (Resume, settings, return to start menu, exit game)
    '''
    def __init__(self):
        self.status = 2
    
    def render(self, game):
        game.window.fill((0, 0, 255))

        return {
            'state': self.status,
            'run': True
        }

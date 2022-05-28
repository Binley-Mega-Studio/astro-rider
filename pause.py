import pygame
from pygame.locals import *

class Pause:
    '''
    Pause menu
    Contents: (Resume, settings, return to start menu, exit game)
    '''
    def __init__(self):
        self.status = 0
    
    def render(self, game):
        game.window.fill((0, 0, 255))

        return {
            'status': self.status,
            'level': None,
            'run': True
        }

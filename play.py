import pygame
from pygame.locals import *

class Play:
    '''
    Actual gameplay
    Contents: (Actual gameplay)
    '''
    def __init__(self):
        self.status = 0

    def render(self, game):
        game.window.fill((0, 255, 0))

        return {
            'status': self.status,
            'level': None,
            'run': True
        }

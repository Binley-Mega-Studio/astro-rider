import pygame
from pygame.locals import *

class Play:
    '''
    Actual gameplay
    Contents: (Actual gameplay)
    '''
    def __init__(self):
        self.status = 1

    def render(self, game):
        game.window.fill((0, 255, 0))

        return {
            'state': self.status,
            'run': True
        }

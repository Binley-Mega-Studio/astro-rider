import pygame
from pygame.locals import *

class Pause:
    '''
    Pause menu
    Contents: (Resume, settings, return to start menu, exit game)
    '''
    def __init__(self):
        self.status = 2
        self.play_btn = pygame.image.load('sprites/play.png').convert_alpha()
        self.logo = pygame.image.load('sprites/astronaut.png').convert_alpha() #Should be the same type anyway but just to double check
        
        
        self.x = 250
        self.y = 250
        
    def render(self, game):
        game.window.fill((0, 0, 255))
        scaled_image = pygame.transform.scale(self.play_btn, (200,200))
        game.window.blit(scaled_image, (self.x, self.y))
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
              pos= pygame.mouse.get_pos()
        if self.play_btn.collidepoint(pos):
            self.status = 1
        return {
            'state': self.status,
            'run': True
        }

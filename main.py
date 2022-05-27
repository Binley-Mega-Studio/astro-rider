import pygame
from pygame.locals import *
from userinterface import menu


a = menu.Menu()
a.say_hello()

pygame.init()
pygame.font.init()


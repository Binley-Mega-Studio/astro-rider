import pygame
from pygame.locals import *
from userinterface import menu, pause, play
 # Initialisation

pygame.init()
pygame.font.init()

display_info = pygame.display.Info()

# Constants
SIZE = WIDTH, HEIGHT = int(display_info.current_w/2), int(display_info.current_h/2)
FPS = 60
run = True

window = pygame.display.set_mode(SIZE)

menu = menu.Menu()



pygame.display.set_caption('Astro Rider')

clock = pygame.time.Clock()

while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
   

        
pygame.quit()
    
    
    
    
    
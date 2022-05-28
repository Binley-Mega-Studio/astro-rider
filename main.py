import pygame
from pygame.locals import *

from pause import Pause
from play import Play
from start import Start

 # Initialisation

pygame.init()
pygame.font.init()

# Constants

FPS = 60
INITIAL_STATUS = 0
GAME_TITLE = 'Astro Rider'

class Game:
    '''
    Status 0: Start menu (Play button, settings, level select, exit game)
    Status 1: In game (Actual gameplay)
    Status 2: Pause menu (Resume, settings, return to start menu, exit game)
    '''
    def __init__(self, fps, title, status):
        
        self.FPS = fps
        self.TITLE = title
        
        self.__status = status # Start menu
        
        display_info = pygame.display.Info()
        self.SIZE = self.WIDTH, self.HEIGHT = int(display_info.current_w/2), int(display_info.current_h/2)
        self.window = pygame.display.set_mode(self.SIZE)
        pygame.display.set_caption(self.TITLE)
        
        self.__start = Start()
        self.__play = Play()
        self.__pause = Pause()
        self.__run = True
        
        self.data = {
            'status': status,
            'level': None,
            'run': True
        }
    
    def run(self):
        clock = pygame.time.Clock()
        
        while self.__run:
            clock.tick(self.FPS)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__quit_game()
                    
            if self.__status == 1:
                self.data = self.__play.render(self)
            elif self.__status == 0:
                self.data = self.__start.render(self)
            elif self.__status == 2:
                self.data = self.__pause.render(self)
            
            self.__status = self.data['status']
            pygame.display.update()
            
            
    def get_data(self):
        return self.data
    
    def __quit_game(self):
        self.__run = False 


if __name__ == '__main__':
    game = Game(
        fps = FPS,
        title = GAME_TITLE,
        status = INITIAL_STATUS
    )
    game.run()
        
pygame.quit()
    
    
    
    
    
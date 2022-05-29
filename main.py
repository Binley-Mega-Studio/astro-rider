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
INITIAL_state = 1
GAME_TITLE = 'Astro Rider'


class Game:
    '''
    state 0: Start menu (Play button, settings, level select, exit game)
    state 1: In game (Actual gameplay)
    state 2: Pause menu (Resume, settings, return to start menu, exit game)
    '''
    def __init__(self, fps, title, state):
        
        self.FPS = fps
        self.TITLE = title
        
        self.__state = state # Start menu   #change back to state just testing
        
        display_info = pygame.display.Info()
        self.SIZE = self.WIDTH, self.HEIGHT = int(display_info.current_w/2), int(display_info.current_h/2)
        self.window = pygame.display.set_mode(self.SIZE)
        pygame.display.set_caption(self.TITLE)
        
        self.level = 1
        
        self.__start = Start()
        self.__play = Play()
        self.__pause = Pause()
        self.__run = True
        
        self.data = {
            'state': state,
            'run': True
        }
    
    def run(self):
        clock = pygame.time.Clock()
        
        while self.__run:
            self.dt = clock.tick(self.FPS) * .001 * self.FPS
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__quit_game()
                    
            if self.__state == 1:
                self.data = self.__play.render(self)
            elif self.__state == 0:
                self.data = self.__start.render(self)
            elif self.__state == 2:
                self.data = self.__pause.render(self)
            
            self.__state = self.data['state']
            pygame.display.update()
            
    def get_data(self):
        return self.data
    
    def __quit_game(self):
        self.__run = False 
        

if __name__ == '__main__':
    game = Game(
        fps = FPS,
        title = GAME_TITLE,
        state = INITIAL_state
    )
    game.run()
        
pygame.quit()
    
    
    
    
    
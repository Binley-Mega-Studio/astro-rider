from pygame.locals import *
from level_1 import Level1

class Level:
    '''
    Level Loader
    Contents: load_level, render
    '''
    def __init__(self):
        self.levels = [Level1]
        self.level_loaded = None
        
    def load_level(self, game):
        if self.level_loaded is None:
            self.level_loaded = self.levels[game.level]
    
    def render(self, game):
        
        self.level_loaded.render(game)


        return {
            'state': self.state,
            'run': True
        }

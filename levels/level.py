from pygame.locals import *
from levels.leveltemplate import Level_Template
class Level:
    '''
    Level Loader
    Contents: load_level, render
    '''
    def __init__(self,game):
        self.level_loaded = None
        self.state = 1
        self.level_template = Level_Template()
    def load_level(self,game):
        self.level_template.populate_planets(game)
        self.level_loaded = True
        
    def render(self, game):
        if self.level_loaded:
           self.level_template.render(game)
        return {
            'state': self.state,
            'run': True
        }
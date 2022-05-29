from pygame.locals import *

from level_template import Level_Template


class Level1(Level_Template):
    def __init__(self):
        super().__init__ ()
        
        self.planet_type = 'Planet_1'
        self.music = 'L1'
        self.planet_pos = [(20,100)]
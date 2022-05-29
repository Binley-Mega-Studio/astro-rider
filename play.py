from pygame.locals import *

from levels import level
from sprites import astronaut


class Play:
    '''
    Actual gameplay
    Contents: (Actual gameplay)
    '''
    def __init__(self,game):
        self.state = 1
        self.player = astronaut.Player()
        self.level = level.Level(game)
        
    def render(self, game):
        
        game.window.fill((0, 0, 0))
        
        #self.planet_data = self.planet.render(game)
        
        self.player_data = self.player.render(game, self)
        

        return {
            'state': self.state,
            'run': True
        }

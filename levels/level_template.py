from pygame.locals import *
from planet import Planet

class Level_Template:
    
    def __init__(self):
        self.planets = []
        self.planet_pos = [(20,100)]
        
    def populate_planets(self,game):
        for x,y in self.planet_pos:
            planet = Planet(self.planet_type,x,y,game)
        
    def render(self, game):
        for planet in self.planets:
            planet.render(game)
        
        #self.planet_data = self.planet.render(game)
        
        self.player_data = self.player.render(game, self)
        
        return {
            'state': self.state,
            'run': True
        }
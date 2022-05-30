from pygame.locals import *
from levels.planet import Planet
import random

class Level_Template:
    
    def __init__(self):
        self.planets = []
        self.planets_imgs = (['Planet_1.png','Planet_2.png','Planet_3.png'],['Planet_2.png','Planet_4.png','Planet_3.png'],['Planet_7.png','Planet_10.png','Planet_9.png'],['Planet_9.png','Planet_7.png','Planet_5.png'])
        self.planet_imgs = random.choice(self.planets_imgs[random.randint(0,3)])
        planetpositions = [[(20,100),(70,150),(10,200)],[(20,100),(70,150),(10,200)],[(20,100),(70,150),(10,200)],[(20,100),(70,150),(10,200)]]
        self.planet_pos = random.choice(planetpositions[random.randint(0,3)])
        
    def populate_planets(self,game):
        for x,y in self.planet_pos:
            self.planets.append(Planet(self.planet_imgs,x,y,game))
            
        
    def render(self, game):
        for planet in self.planets:
            planet.render(game)
        
        #self.planet_data = self.planet.render(game)
        
        self.player_data = self.player.render(game, self)
        
        return {
            'state': self.state,
            'run': True
        }
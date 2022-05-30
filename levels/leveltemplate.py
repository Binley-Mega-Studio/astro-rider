from pygame.locals import *
from levels.planet import Planet
import random

class Level_Template:
    
    def __init__(self):
        self.planets = []
        self.planets_imgs = [['Planet_1.png','Planet_2.png','Planet_3.png'],['Planet_2.png','Planet_4.png','Planet_3.png'],['Planet_7.png','Planet_10.png','Planet_9.png'],['Planet_9.png','Planet_7.png','Planet_5.png']]
        self.planet_imgs = random.choice(self.planets_imgs)
        planetpositions = [[(200,50),(500,300),(640,50)],[(200,50),(500,300),(640,50)],[(200,50),(500,300),(640,50)],[(200,50),(500,300),(640,50)]]
        self.planet_pos = random.choice(planetpositions)
        self.state = 1
        
    def populate_planets(self,game):
        index = 0
        for x,y in self.planet_pos:
            self.planets.append(Planet(self.planet_imgs[index],x,y,game))
            index += 1
        
    def render(self, game):
        for planet in self.planets:
            planet.render(game)
        

        
        return {
            'state': self.state,
            'run': True
        }
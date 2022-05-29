import pygame
import math

# newtons equations of motion
# v = prev_v + a * dt
# p = prev_p + (v * dt) + (.5 * a * dt^2)


class Player(pygame.sprite.Sprite):
    '''
    Spawn player
    '''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.active = True # Player is actively being moved
        self.image = pygame.image.load('sprites/astronaut.png')
        self.rect = self.image.get_rect()
  
        self.x = 0
        self.y = 0
        self.angle = 0
        
        self.HEIGHT = 100
        self.WIDTH = 100
        self.distance_x, self.distance_y = 0, 0
        self.distance = 0
        
        self.gravity = 0 # changes with position to planet
        self.acceleration = pygame.math.Vector2(0, self.gravity)
        
    def render(self, game, play_data):
        
        scaled_image = pygame.transform.scale(self.image, (self.WIDTH, self.HEIGHT))
        rotated_image = pygame.transform.rotate(scaled_image, 360 - self.angle)
        
        if self.distance:
            self.distance -= 1
            self.x += self.distance_x
            self.y += self.distance_y
            
        #game.window.blit(scaled_image, (self.x, self.y))
        game.window.blit(rotated_image, (self.x - int(rotated_image.get_width() /2), self.y - int(rotated_image.get_height() /2))) #changed
        self.update(game)
        
        return None
        
    def update(self,game):
        
        mouse = pygame.mouse.get_pos()
        self.a = mouse[1] - (self.y + self.HEIGHT / 2)
        self.b = mouse[0] - (self.x + self.WIDTH / 2)
        
        radians = math.atan2(mouse[1] - (self.y), mouse[0] - (self.x))

        self.angle = math.degrees(radians)
        
        self.distance = int(math.hypot(mouse[1] - (self.y + self.HEIGHT / 2), mouse[0] - (self.x + self.WIDTH / 2)))
        
        self.distance_x, self.distance_y = math.cos(radians), math.sin(radians)
        
        

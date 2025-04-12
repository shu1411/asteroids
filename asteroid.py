import pygame
import random

from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    
    def update(self, dt):
        self.position += self.velocity * dt


    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        ast_pos1 = self.velocity.rotate(angle)
        ast_pos2 = self.velocity.rotate(-angle)
        new_ast_radius = self.radius - ASTEROID_MIN_RADIUS
        ast1 = Asteroid(self.position.x, self.position.y, new_ast_radius)
        ast2 = Asteroid(self.position.x, self.position.y, new_ast_radius)
        ast1.velocity = ast_pos1 * 1.2
        ast2.velocity = ast_pos2 * 1.2
        

    

from circleshape import CircleShape
import pygame
from constants import *

class Shot(CircleShape):
    def __init__(self,x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self,screen):
        # pygame.draw.circle(self.position, radius=self.radius, width=2)
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt # ask if i should use super()
import random

from circleshape import CircleShape
import pygame
from constants import *


class Asteroid(CircleShape):
    def __init__(self,x, y, radius):
        super().__init__(x, y, radius)

    def draw(self,screen):
        # pygame.draw.circle(self.position, radius=self.radius, width=2)
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt # ask if i should use super()

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return

        if self.radius >= ASTEROID_MIN_RADIUS:
            self.kill()
            angle = random.uniform(20,50)
            asteroid_veloc_1 = self.velocity.rotate(angle)
            asteroid_veloc_2 = self.velocity.rotate(-angle)

            radius_after_split = self.radius - ASTEROID_MIN_RADIUS
            asteroid_n1 = Asteroid(self.position.x, self.position.y, radius_after_split)
            asteroid_n2 = Asteroid(self.position.x, self.position.y, radius_after_split)
            asteroid_n1.velocity = asteroid_veloc_1 * 1.2
            asteroid_n2.velocity = asteroid_veloc_2 * 1.2
            return


import pygame
from circleshape import CircleShape

from constants import LINE_WIDTH


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        return

    def update(self, dt):
        self.position += self.velocity * dt
        return

    def collides_with(self, other: CircleShape):
        return super().collides_with(other)

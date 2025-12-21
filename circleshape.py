import pygame
from typing import Self


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position: pygame.math.Vector2 = pygame.math.Vector2(x, y)
        self.velocity: pygame.math.Vector2 = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen: pygame.Surface):
        # must override
        pass

    def update(self, dt):
        # must override
        pass

    def collides_with(self, other: Self):
        distance = self.position.distance_to(other.position)
        if distance < (self.radius + other.radius):
            return True
        return False

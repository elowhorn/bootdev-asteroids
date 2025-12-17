import pygame
from circleshape import CircleShape
from shot import Shot
from constants import (
    PLAYER_RADIUS,
    LINE_WIDTH,
    PLAYER_SHOOT_COOLDOWN_SECONDS,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    PLAYER_SHOOT_SPEED,
)


class Player(CircleShape):

    def __init__(self, x, y):
        self.rotation = 0
        self.cooldown_timer = 0
        super().__init__(x, y, PLAYER_RADIUS)

    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen: pygame.Surface):
        points = self.triangle()
        pygame.draw.polygon(screen, "white", points, LINE_WIDTH)
        return

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        return

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
        return

    def shoot(self):
        if self.cooldown_timer > 0:
            return
        self.cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
        position: pygame.Vector2 = self.position
        shot = Shot(position.x, position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

    def update(self, dt):
        keys = pygame.key.get_pressed()

        self.cooldown_timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        return

    def collides_with(self, other: CircleShape):
        return super().collides_with(other)

import pygame

from constants import *



# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        pass

    def collision(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius

    def wrap_position(self):
        self.position.x = self.position.x % 1550
        self.position.y = ((self.position.y - 50) % (965 - 50)) + 50

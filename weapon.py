import pygame
from constants import *

class Weapon(pygame.sprite.Sprite):
    def __init__(self,fire_range,fire_rate,radius):
        self.fire_range = fire_range
        self.fire_rate = fire_rate
        self.radius = radius

    def draw(self):
        pass

    def update(self):
        pass


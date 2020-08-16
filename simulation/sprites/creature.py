import pygame
from pygame.sprite import Sprite
import random


class Creature(Sprite):
    image = pygame.image.load('static/creature.png')
    image.set_colorkey(image.get_at((0, 0)))

    def __init__(self, fps, x, y, food, *groups):
        super(Creature, self).__init__(*groups)
        self.image = Creature.image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, x)
        self.rect.y = random.randint(0, y)
        self.set_characteristics(fps)
        self.food = food

    def set_characteristics(self, fps):
        self.speed = 240 / fps
        self.max_energy = 600
        self.energy = self.max_energy

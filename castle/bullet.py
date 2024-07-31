from pygame.sprite import Sprite
from constants import *
import pygame
import math
class Bullet(Sprite):
    def __init__(self, x,y, group, degree,size):
        super().__init__()
        self.image = pygame.transform.scale(bullet,(size,size))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        group.add(self)
        self.degree = degree
        
    def update(self)    :
        self.rect.x += math.cos(self.degree) * 5
        self.rect.y += -math.sin(self.degree) * 5


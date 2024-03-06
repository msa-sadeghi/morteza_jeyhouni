from constants import *
from pygame.sprite import Sprite
class Lava(Sprite):
    def __init__(self, image, x,y):
        super().__init__()
        self.image = pygame.transform.scale(image, (32,32))
        self.rect = self.image.get_rect(topleft = (x,y))


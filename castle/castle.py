from pygame.sprite import Sprite
from constants import *
class Castle(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.health = 100
        self.max_health = 100
        w = castle_100.get_width()
        h = castle_100.get_height()
        self.image_100 = pygame.transform.scale(castle_100, (w * 0.2, h * 0.2))
        self.image_50 = pygame.transform.scale(castle_50, (w * 0.2, h * 0.2))
        self.image_25 = pygame.transform.scale(castle_25, (w * 0.2, h * 0.2))
        self.image = self.image_100
        self.rect = self.image.get_rect(topleft=(x,y))
        
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
from pygame.sprite import Sprite
import pygame
from bullet import Bullet
import math
class Tower(Sprite):
    def __init__(self, x,y, group):
        super().__init__()
        self.all_images = []
        
        for i in ('25', '50', '100'):
            img = pygame.image.load(f"assets/tower/tower_{i}.png")
            img_w = img.get_width()
            img_h = img.get_height()
            img = pygame.transform.scale(img, (img_w * 0.2, img_h * 0.2))
            self.all_images.append(img)
            
        self.image = self.all_images[2]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        group.add(self)
        self.last_shoot_time = 0
    def update(self, enemy_group, bullet_group):
        for enemy in enemy_group:
            if self.rect.x - enemy.rect.x < 400 and enemy.alive:
                ydist = -(enemy.rect.bottom - self.rect.y)
                xdist = enemy.rect.right - self.rect.x
                deg = math.atan2(ydist, xdist)
                if pygame.time.get_ticks() - self.last_shoot_time > 1500:
                    self.last_shoot_time = pygame.time.get_ticks()
                    Bullet(self.rect.x, self.rect.y, bullet_group, deg, 24)
        
            
            
            
            
from pygame.sprite import Sprite
import pygame

class Enemy(Sprite):
    def __init__(self, enemy_type, health, speed, x,y, group, scale):
        super().__init__()
        self.enemy_type = enemy_type
        self.health = health
        self.speed = speed
        self.alive = True
        self.all_images = {}
        self.animation_types = ("walk", "attack", "death")
        for animation in self.animation_types:
            temp_list = []
            for i in range(20):
                img = pygame.image.load(f"assets/enemies/{self.enemy_type}/{animation}/{i}.png")
                w = img.get_width()
                h = img.get_height()
                img = pygame.transform.scale(img, (w * scale, h * scale))
                temp_list.append(img)
            self.all_images[animation] = temp_list
        self.action = "walk"
        self.image_number = 0
        self.image = self.all_images[self.action][self.image_number]
        self.rect = self.image.get_rect(topleft = (x,y))
        group.add(self)
        
    def update(self):
        self.rect.x += self.speed
        
                
            
            
        
        
        
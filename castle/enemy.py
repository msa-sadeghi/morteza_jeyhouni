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
        self.last_anim_time = pygame.time.get_ticks()
        group.add(self)
        
    def update(self, castle):
        if self.rect.right > castle.rect.left:
            self.update_action("attack")
        if self.action == "walk":
            self.rect.x += self.speed
        self.animation()
        
    def animation(self):
        self.image = self.all_images[self.action][self.image_number]
        if pygame.time.get_ticks() - self.last_anim_time > 100:
            self.last_anim_time = pygame.time.get_ticks()
            self.image_number += 1
            if self.image_number >= len(self.all_images[self.action]):
                self.image_number = 0
        
    def update_action(self, n)    :
        if self.action != n:
            self.action = n
        
                
            
            
        
        
        
from pygame.sprite import Sprite
import pygame
import os
class Soldier(Sprite):
    def __init__(self, x,y , scale):
        super().__init__()
        self.animation_list = []
        self.image_number = 0
        self.action = 0
        animation_types = ("Idle", "Run", "Jump", "Death")
        for animation in animation_types:
            images = []
            num_of_images = len(os.listdir(f"assets/img/player/{animation}"))
            for i in range(num_of_images):
                img = pygame.image.load(f"assets/img/player/{animation}/{i}.png")
                w = img.get_width()
                h = img.get_height()
                img = pygame.transform.scale(img, (w*scale, h*scale))
                images.append(img)
            self.animation_list.append(images)
        self.image = self.animation_list[self.action][self.image_number]
        self.rect = self.image.get_rect(center=(x,y))
        self.speed = 5
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def move(self, left, right):
        dx = 0
        dy = 0
        
        if left:
            dx -= self.speed
        if right:
            dx += self.speed
            
        self.rect.x += dx
        self.rect.y += dy
            
        
    
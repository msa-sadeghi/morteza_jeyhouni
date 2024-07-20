from pygame.sprite import Sprite
import pygame
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
    def update(self):
        pass
        
            
            
            
            
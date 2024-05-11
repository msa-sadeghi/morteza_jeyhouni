from pygame.sprite import Sprite
from constants import *
from bullet import Bullet
import math
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
        self.shoot_ = False   
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def shoot(self, bullet_group):
        if pygame.mouse.get_pressed()[0] and not self.shoot_:
            self.shoot_ = True
            mouse_position = pygame.mouse.get_pos()
            y_dis = -(mouse_position[1] - self.rect.midleft[1])
            x_dis = mouse_position[0] - self.rect.midleft[0]
            degree = math.atan2(y_dis, x_dis)
            
            Bullet(self.rect.midleft[0], self.rect.midleft[1], bullet_group, degree)
        if not pygame.mouse.get_pressed()[0]:
            self.shoot_ = False
        
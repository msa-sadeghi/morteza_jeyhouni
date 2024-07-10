from pygame.sprite import Sprite
from constants import *
from bullet import Bullet
import math
from healthbar import HealthBar
class Castle(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.health = 100
        self.money = 0
        self.score = 0
        self.max_health = 100
        w = castle_100.get_width()
        h = castle_100.get_height()
        self.image_100 = pygame.transform.scale(castle_100, (w * 0.2, h * 0.2))
        self.image_50 = pygame.transform.scale(castle_50, (w * 0.2, h * 0.2))
        self.image_25 = pygame.transform.scale(castle_25, (w * 0.2, h * 0.2))
        self.image = self.image_100
        self.rect = self.image.get_rect(topleft=(x,y)) 
        self.shoot_ = False 
        self.healthbar = HealthBar(self.rect.centerx, self.rect.top, self.health, self.max_health)  
    def draw(self, screen):
        self.healthbar.update(screen, self.health)
        if self.health <= 25:
            self.image = self.image_25
        elif self.health <= 50:
            self.image = self.image_50
        else: 
            self.image = self.image_100
        screen.blit(self.image, self.rect)
        font = pygame.font.SysFont("arial", 22)
        health = font.render(f"Health: {self.health}", True, (240,70,10))
        screen_width = screen.get_width()
        screen_heigth = screen.get_height()
        screen.blit(health, (screen_width - self.rect.size[0]/2, 500))
    def shoot(self, bullet_group):
        if pygame.mouse.get_pressed()[0] and not self.shoot_ :
            self.shoot_ = True
            mouse_position = pygame.mouse.get_pos()
            y_dis = -(mouse_position[1] - self.rect.midleft[1])
            x_dis = mouse_position[0] - self.rect.midleft[0]
            degree = math.atan2(y_dis, x_dis)
            if mouse_position[1] > 70:
                Bullet(self.rect.midleft[0], self.rect.midleft[1], bullet_group, degree)
        if not pygame.mouse.get_pressed()[0]:
            self.shoot_ = False
            
    def repair(self):
        if self.money >= 10:
            self.health += 30
            self.money -= 10
            if self.health > self.max_health:
                self.health = self.max_health
                
    def armour(self):
        if self.money >= 1000:
            self.max_health += self.max_health * 0.2
            
        
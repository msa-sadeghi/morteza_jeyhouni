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
        self.last_attack_time = pygame.time.get_ticks()
        group.add(self)
        
    def update(self, castle, bullet_group, screen):
        if self.alive:
            if pygame.sprite.spritecollide(self, bullet_group, True):
                self.health -= 25
            if self.health <= 0:
                castle.money += 100
                castle.score += 150
                self.update_action("death")
                self.alive = False
                
        if self.rect.right > castle.rect.left:
            self.update_action("attack")
        if self.action == "walk":
            self.rect.x += self.speed
            
        if self.action == "attack":
            if pygame.time.get_ticks() - self.last_attack_time > 1000:
                self.last_attack_time = pygame.time.get_ticks()
                castle.health -= 1
                if castle.health < 0:
                    castle.health = 0
            
        self.animation()
        if self.alive:
            font = pygame.font.SysFont("arial", 22)
            health_text = font.render(str(self.health), True, (255,0,0))
            rect = health_text.get_rect(bottom = self.rect.top, centerx=self.rect.centerx)
            screen.blit(health_text, rect)
        
    def animation(self):
        self.image = self.all_images[self.action][self.image_number]
        if pygame.time.get_ticks() - self.last_anim_time > 100:
            self.last_anim_time = pygame.time.get_ticks()
            self.image_number += 1
            if self.image_number >= len(self.all_images[self.action]):
                if self.action == "death":
                    self.image_number = len(self.all_images[self.action]) - 1
                else:
                    self.image_number = 0
        
    def update_action(self, n)    :
        if self.action != n:
            self.action = n
        
                
            
            
        
        
        
from constants import *
from pygame.sprite import Sprite


class Player(Sprite):
    def __init__(self,x,y):
        self.reset(x,y)
    
    def reset(self,x,y):
        self.right_images = []
        self.left_images = []
        for i in range(1,5):
            image = pygame.image.load(f"assets/img/guy{i}.png")
            self.right_images.append(image)
            image = pygame.transform.flip(image, True, False)
            self.left_images.append(image)
        self.y_velocity = 0
        self.direction = 1
        self.speed = 5
        self.image = self.right_images[0]
        self.rect = self.image.get_rect(topleft = (x,y))
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.idle = True
        self.jumped = False
        self.in_air = False
        self.jump_sound = pygame.mixer.Sound("assets/img/jump.wav")
        self.alive = True
        self.dead_image = pygame.image.load("assets/img/ghost.png")
    
    def draw(self):
        SCREEN.blit(self.image, self.rect)
    def animation(self):
        if pygame.time.get_ticks() - self.update_time > 200:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= len(self.right_images):
                self.frame_index = 0
        if self.direction == 1 and not self.idle:
            self.image = self.right_images[self.frame_index]
        if self.direction == -1 and not self.idle:
            self.image = self.left_images[self.frame_index]
        if self.idle:
            if self.direction == 1:
                self.image = self.right_images[0]
            if self.direction == -1:
                self.image = self.left_images[0]
    def move(self, tile_map, enemy_group):
        dx = 0
        dy = 0
        if self.alive:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.idle = False
                self.direction = -1
                dx -= self.speed
            if keys[pygame.K_RIGHT]:
                self.idle = False
                self.direction = 1
                dx += self.speed
            if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                self.idle = True
            if keys[pygame.K_SPACE] and not self.jumped and not self.in_air:
                self.jumped = True
                self.in_air = True
                self.y_velocity = -17
                self.jump_sound.play()
            if not  keys[pygame.K_SPACE]:
                self.jumped = False  
            self.y_velocity += 1
            dy += self.y_velocity
            for tile in tile_map:
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.image.get_width(), self.image.get_height()):
                    dx = 0
                if tile[1].colliderect(self.rect.x, self.rect.y + dy,
                                    self.image.get_width(), self.image.get_height()):
                    if self.y_velocity > 0:
                        self.y_velocity = 0
                        dy = tile[1].top - self.rect.bottom
                        self.in_air = False
                    elif self.y_velocity < 0:
                        self.y_velocity = 0
                        dy = tile[1].bottom - self.rect.top
            self.animation()
            if pygame.sprite.spritecollide(self, enemy_group, False):
                self.alive = False
        else:
            self.image = self.dead_image
            if self.rect.top > 200:
                self.rect.y -= 5
            
                    
        self.rect.x += dx
        self.rect.y += dy
        



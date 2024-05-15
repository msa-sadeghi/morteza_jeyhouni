import pygame
from constants import *
from castle import Castle
from enemy import Enemy
import random
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
enemies_health = (100, 125, 150, 175)
enemies_type = ('knight', 'goblin','purple_goblin', 'red_goblin')
level_difficulty = 0
max_difficulty = 1000
enemy_group = pygame.sprite.Group()
castle = Castle(SCREEN_WIDTH - 280, SCREEN_HEIGHT - 350)
bullet_group = pygame.sprite.Group()
last_enemy_spawn_time = pygame.time.get_ticks()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
FPS = 60
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if level_difficulty <= max_difficulty:
        if pygame.time.get_ticks() - last_enemy_spawn_time > 2000:
            last_enemy_spawn_time = pygame.time.get_ticks()
            i = random.randrange(len(enemies_type))
            Enemy(enemies_type[i], enemies_health[i], 1, 100, random.choice([300,350,400,450,500,510]), enemy_group, 0.2)
            level_difficulty += enemies_health[i]    
    
    
    screen.blit(bg, (0,0)) 
    castle.draw(screen) 
    castle.shoot(bullet_group) 
    bullet_group.draw(screen)     
    bullet_group.update()
    enemy_group.draw(screen)     
    enemy_group.update(castle)
    pygame.display.update()
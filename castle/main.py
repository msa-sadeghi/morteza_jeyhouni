import pygame
from constants import *
from castle import Castle
from enemy import Enemy
import random
from button import Button


pygame.init()

repair_image = pygame.image.load("assets/repair.png")
repair_button = Button(repair_image, 600, 20)
armour_image = pygame.image.load("assets/armour.png")
armour_button = Button(armour_image, 660, 20)
screen = pygame.display.set_mode()

SCREEN_WIDTH = screen.get_width()

SCREEN_HEIGHT = screen.get_height()
bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
enemies_health = (100, 125, 150, 175)
enemies_type = ('knight', 'goblin','purple_goblin', 'red_goblin')
level_difficulty = 0
max_difficulty = 1000
enemy_group = pygame.sprite.Group()
castle = Castle(SCREEN_WIDTH - 280, SCREEN_HEIGHT - 350)
bullet_group = pygame.sprite.Group()
last_enemy_spawn_time = pygame.time.get_ticks()
clock = pygame.time.Clock()

font = pygame.font.SysFont("arial", 48)
next_level_text = font.render("WELCOME TO NEW LEVEL 1", True, (255, 20,10))
next_level_rect = next_level_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 80))

score_text = font.render(f"Score : {castle.score}", True, (255, 20,10))
score_rect = next_level_text.get_rect(topleft=(0,0))
money_text = font.render(f"money : {castle.money}", True, (255, 20,10))
money_rect = next_level_text.get_rect(topleft=(300,0))



FPS = 60
level = 1
next_level = False
level_reset_time = 0
running = True
while running:
    screen.blit(bg, (0,0)) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    if level_difficulty <= max_difficulty:
        if pygame.time.get_ticks() - last_enemy_spawn_time > 2000:
            last_enemy_spawn_time = pygame.time.get_ticks()
            i = random.randrange(len(enemies_type))
            Enemy(enemies_type[i], enemies_health[i], 1, 100, random.choice([600,650,700,750,800,810]), enemy_group, 0.2)
            level_difficulty += enemies_health[i]    
    else:
        number_of_enemies = 0
        
        for enemy in enemy_group:
            if enemy.alive:
                number_of_enemies += 1
        if number_of_enemies == 0 and next_level == False: 
            next_level = True    
            level_reset_time = pygame.time.get_ticks() 
            
            
    if next_level:
        next_level_text = font.render(f"WELCOME TO NEW LEVEL {level+1}", True, (255, 20,10))
        screen.blit(next_level_text, next_level_rect) 
        if pygame.time.get_ticks() - level_reset_time > 1500:
            next_level = False
            enemy_group.empty()
            level += 1
            max_difficulty = max_difficulty + 0.1 * max_difficulty
            level_difficulty = 0
    score_text = font.render(f"Score : {castle.score}", True, (255, 20,10))
    money_text = font.render(f"money : {castle.money}", True, (255, 20,10))
    screen.blit(score_text, score_rect)
    screen.blit(money_text, money_rect)
    castle.draw(screen) 
    castle.shoot(bullet_group) 
    bullet_group.draw(screen)     
    bullet_group.update()
    enemy_group.draw(screen)     
    enemy_group.update(castle, bullet_group,screen)
    repair_button.draw(screen)
    if repair_button.click():
        castle.repair()
        
    armour_button.draw(screen)
    if armour_button.click():
        castle.armour()
    pygame.display.update()
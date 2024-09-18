import pygame
from solider import Soldier
screen_width = 800
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
FPS = 60
player = Soldier(100, 300, 2)
bg_image = pygame.image.load("assets/img/dragon.jpg")
bg_image = pygame.transform.rotate(bg_image, 90)
bg_rect = bg_image.get_rect()
bg_rect.center = (screen_width//2, screen_height//2)
start_time = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    if pygame.time.get_ticks() - start_time <= 2000:
        screen.blit(bg_image, bg_rect)
    else:    
        player.draw(screen)
    
    pygame.display.update()
    clock.tick(FPS)

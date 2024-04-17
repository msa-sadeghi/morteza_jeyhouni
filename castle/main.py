import pygame
from constants import *
from castle import Castle
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


castle = Castle(SCREEN_WIDTH - 280, SCREEN_HEIGHT - 350)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(bg, (0,0)) 
    castle.draw(screen)       
    pygame.display.update()
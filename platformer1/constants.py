import pygame
from pygame.sprite import Sprite
pygame.init()

SCREEN = pygame.display.set_mode()
SCREEN_WIDTH = SCREEN.get_width()
SCREEN_HEIGHT = SCREEN.get_height()
TILE_SIZE = 32
ROWS = SCREEN_HEIGHT // TILE_SIZE
COLS = SCREEN_WIDTH // TILE_SIZE
print(ROWS)
print(COLS)

bg_image = pygame.image.load("assets/background.png")
bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))


dirt_image = pygame.image.load("assets/dirt.png")
grass_image = pygame.image.load("assets/grass.png")
water_image = pygame.image.load("assets/water.png")
lava_image = pygame.image.load("assets/img/lava.png")
door_image = pygame.image.load("assets/img/exit.png")


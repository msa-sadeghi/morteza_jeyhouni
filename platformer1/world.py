from constants import *
from enemy import Enemy
class World:
    def __init__(self, data, enemy_group):
        self.tile_map = []

        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] == 1:
                    img = dirt_image
                    rect = img.get_rect()
                    rect.topleft = (j * TILE_SIZE, i * TILE_SIZE)
                    tile = (img, rect)
                    self.tile_map.append(tile)
                if data[i][j] == 2:
                    img = grass_image
                    rect = img.get_rect()
                    rect.topleft = (j * TILE_SIZE, i * TILE_SIZE)
                    tile = (img, rect)
                    self.tile_map.append(tile)
                if data[i][j] == 5:
                    Enemy(j * TILE_SIZE, i * TILE_SIZE, enemy_group)


    def draw(self):
        for tile in self.tile_map:
            SCREEN.blit(tile[0], tile[1])
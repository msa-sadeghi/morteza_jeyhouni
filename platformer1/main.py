from constants import *
from world import World
from level1 import world_data
from player import Player
from button import Button

enemy_group = pygame.sprite.Group()

game_world = World(world_data,enemy_group)
my_player = Player(100, 300)

FPS = 60
clock = pygame.time.Clock()

restart_btn_img = pygame.image.load("assets/img/restart_btn.png")

restart_btn = Button(restart_btn_img, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    SCREEN.blit(bg_image, (0,0))
    
    
    if my_player.alive == False:
        restart_btn.draw()
    else:
        game_world.draw()
        my_player.move(game_world.tile_map, enemy_group)
        enemy_group.update()
        my_player.draw()
        enemy_group.draw(SCREEN)
    pygame.display.update()
    clock.tick(FPS)

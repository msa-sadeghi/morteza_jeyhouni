from constants import *
from world import World
from level_creator import world_data
from player import Player
from button import Button


def reset_game():
    my_player.reset(100,300)

enemy_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
door_group = pygame.sprite.Group()

game_world = World(world_data,enemy_group, lava_group, door_group)
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
        if restart_btn.draw():
            reset_game()
    else:
        enemy_group.update()
        game_world.draw()
        enemy_group.draw(SCREEN)
        lava_group.draw(SCREEN)
        door_group.draw(SCREEN)
    if my_player.next_level == True:
        print("*************************************")
    my_player.move(game_world.tile_map, enemy_group, lava_group,door_group)
    my_player.draw()
    
    pygame.display.update()
    clock.tick(FPS)

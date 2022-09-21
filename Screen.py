import pygame
import Consts
import Trash

WINDOW = Consts.WINDOW

def move_robot(keys_pressed):
    direction = ""
    if keys_pressed[pygame.K_LEFT]:  # LEFT
        direction = Consts.LEFT
    if keys_pressed[pygame.K_RIGHT]:  # RIGHT
        direction = Consts.RIGHT
    if keys_pressed[pygame.K_UP]:  # UP
        direction = Consts.UP
    if keys_pressed[pygame.K_DOWN]:  # DOWN
        direction = Consts.DOWN
    return direction

def slide_robot():
    while()




def update_starter_screen():
    WINDOW.blit(Consts.BACKGROUND_IMG, (0, 0))
    trash_array = Trash.get_trash()

    for row in trash_array:



    ship_data = pygame.transform.scale(Consts.SHIP_IMAGE, (Consts.SHIP_WIDTH_IMAGE, Consts.SHIP_HEIGHT_IMAGE))
    ship = pygame.Rect(index_to_pixels(Consts.SHIP_LOCATION), (Consts.SHIP_WIDTH_IMAGE, Consts.SHIP_HEIGHT_IMAGE))
    WINDOW.blit(ship_data, (ship.x, ship.y))

    player_data = pygame.transform.scale(Consts.PLAYER_IMG, (Consts.PLAYER_WIDTH, Consts.PLAYER_HEIGHT))
    player = pygame.Rect(index_to_pixels(player_index), (Consts.PLAYER_WIDTH, Consts.PLAYER_HEIGHT))
    WINDOW.blit(player_data, (player.x, player.y))

    guard_data = pygame.transform.scale(Consts.GUARD_IMG, (Consts.PLAYER_WIDTH, Consts.PLAYER_HEIGHT))
    guard = pygame.Rect(index_to_pixels(guard_index),(Consts.PLAYER_WIDTH, Consts.PLAYER_HEIGHT))
    WINDOW.blit(guard_data, (guard.x, guard.y))

    pygame.display.update()
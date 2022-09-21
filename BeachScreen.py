import pygame
import BeachTrash
import Consts

WINDOW = Consts.WINDOW

def update_beach_screen():
    background_data = pygame.transform.scale(Consts.BEACH_BACKGROUND, (Consts.WINDOW_WIDTH, Consts.WINDOW_HEIGHT))
    background = pygame.Rect((0, 0),
                       (Consts.WINDOW_WIDTH, Consts.WINDOW_HEIGHT))
    WINDOW.blit(background_data, background)
    # WINDOW.blit(Consts.BEACH_BACKGROUND, (0, 0))

    trash_list = BeachTrash.get_trash_beach()
    for i in trash_list:
        for j in i:
            if j != Consts.EMPTY:
                ship_data = pygame.transform.scale(Consts.TRASH_IMAGES[j], (30, 30))
                ship = pygame.Rect(index_to_pixels((i.index(j), trash_list.index(i))), (30, 30))
                WINDOW.blit(ship_data, (ship.x, ship.y))

    pygame.display.update()
    pygame.time.wait(5000)

def index_to_pixels(index):
   return (index[0] * 50, (Consts.WINDOW_HEIGHT / 2 + 55) + index[1] * 50)

t = BeachTrash.generate_trash()
update_beach_screen()
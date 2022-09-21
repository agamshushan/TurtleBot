import pygame
import Consts
import Trash
import TurtleBot

WINDOW = Consts.WINDOW
robot_pixel_x, robot_pixel_y = 0, 0

def move_robot(keys_pressed):
    direction = ""
    global robot_pixel_x
    global robot_pixel_y
    if keys_pressed[pygame.K_LEFT]:  # LEFT
        if TurtleBot.move_bot(Consts.LEFT):
            for i in range(Consts.ROBOT_WIDTH):
                robot_pixel_x -= 1
                update_starter_screen()
    if keys_pressed[pygame.K_RIGHT]:  # RIGHT
        if TurtleBot.move_bot(Consts.RIGHT):
            for i in range(Consts.ROBOT_WIDTH):
                robot_pixel_x += 1
                update_starter_screen()
    if keys_pressed[pygame.K_UP]:  # UP
        if TurtleBot.move_bot(Consts.UP):
            for i in range(Consts.ROBOT_HEIGHT):
                robot_pixel_x -= 1
                update_starter_screen()
    if keys_pressed[pygame.K_DOWN]:  # DOWN
        if TurtleBot.move_bot(Consts.DOWN):
            for i in range(Consts.ROBOT_HEIGHT):
                robot_pixel_x += 1
                update_starter_screen()


def index_to_pixels(x_index, y_index):
    return (x_index * 50, y_index * 100 + 100)


def update_starter_screen():
    WINDOW.blit(Consts.BACKGROUND_IMG, (0, 0))
    trash_array = Trash.get_trash()
    global robot_pixel_y
    global robot_pixel_x

    for i in range(Consts.TURTLE_AMOUNT):
        if i % 2 != 0:
            row = trash_array[-1::-1]
            turtle_data = pygame.transform.rotate(pygame.transform.scale(Consts.TURTLE_IMAGE, (
                Consts.ROBOT_WIDTH, Consts.ROBOT_HEIGHT)), 90)
            turtle = pygame.Rect(index_to_pixels(0, i),
                                 (Consts.ROBOT_WIDTH, Consts.ROBOT_HEIGHT))
            WINDOW.blit(turtle_data, (turtle.x, turtle.y))
        else:
            turtle_data = pygame.transform.rotate(pygame.transform.scale(Consts.TURTLE_IMAGE, (
                Consts.ROBOT_WIDTH, Consts.ROBOT_HEIGHT)), 270)
            turtle = pygame.Rect(index_to_pixels(19, i),
                                 (Consts.ROBOT_WIDTH, Consts.ROBOT_HEIGHT))
            WINDOW.blit(turtle_data, (turtle.x, turtle.y))
        for j in range(len(row)):
            if j != Consts.EMPTY:
                data = pygame.transform.scale(Consts.TRASH_IMAGES[j], (
                Consts.TRASH_WIDTH, Consts.TRASH_HEIGHT))
                trash = pygame.Rect((index_to_pixels(j, i)[0], index_to_pixels(j, i)[1] + 25), (Consts.TRASH_WIDTH, Consts.TRASH_HEIGHT))
                WINDOW.blit(data, (trash.x, trash.y))



    robot_data = pygame.transform.scale(Consts.TURTLE_BOT_IMAGE, (Consts.ROBOT_WIDTH, Consts.ROBOT_HEIGHT))
    robot = pygame.Rect((robot_pixel_x, robot_pixel_y), (Consts.ROBOT_WIDTH, Consts.ROBOT_HEIGHT))
    WINDOW.blit(robot_data, (robot.x, robot.y))

    pygame.display.update()
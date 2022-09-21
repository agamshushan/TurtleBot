import pygame
import Consts
import Trash
import TurtleBot
import Game


def index_to_pixels(x_index, y_index):
    return x_index * 50, y_index * 100 + 100


WINDOW = Consts.WINDOW
# MSG_WINDOW = Consts.MSG_WINDOW
robot_pixel_x, robot_pixel_y = index_to_pixels(TurtleBot.get_loc()[0], TurtleBot.get_loc()[1])


def move_robot(keys_pressed):
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
                robot_pixel_y -= 1
                update_starter_screen()
    if keys_pressed[pygame.K_DOWN]:  # DOWN
        if TurtleBot.move_bot(Consts.DOWN):
            for i in range(Consts.ROBOT_HEIGHT):
                robot_pixel_y += 1
                update_starter_screen()


def update_starter_screen():
    background_data = pygame.transform.scale(Consts.BACKGROUND, (Consts.WINDOW_WIDTH, Consts.WINDOW_HEIGHT))
    background = pygame.Rect((0, 0), (Consts.WINDOW_WIDTH, Consts.WINDOW_HEIGHT))
    WINDOW.blit(background_data, (background.x, background.y))
    trash_array = Trash.get_trash()
    global robot_pixel_y
    global robot_pixel_x

    font = pygame.font.SysFont(Consts.FONT_NAME, Consts.LOSE_FONT_SIZE)
    score_msg = Game.get_score_message()
    text_img = font.render(score_msg, True, Consts.BLACK)
    WINDOW.blit(text_img, (400, 10))

    for i in range(Consts.TURTLE_AMOUNT):
        row = trash_array[i]
        for j in range(len(row)):
            if row[j] != Consts.EMPTY:
                data = pygame.transform.scale(Consts.TRASH_IMAGES[row[j]], (Consts.TRASH_WIDTH, Consts.TRASH_HEIGHT))
                trash = pygame.Rect((index_to_pixels(j, i)[0], index_to_pixels(j, i)[1] + 25), (Consts.TRASH_WIDTH, Consts.TRASH_HEIGHT))
                WINDOW.blit(data, (trash.x, trash.y))
        turtle_data = pygame.transform.rotate(pygame.transform.scale(Consts.TURTLE_IMAGE, (
            Consts.TURTLE_WIDTH, Consts.TURTLE_HEIGHT)), 180)
        turtle = pygame.Rect(index_to_pixels(19, i),
                             (Consts.TURTLE_WIDTH, Consts.TURTLE_HEIGHT))
        WINDOW.blit(turtle_data, (turtle.x, turtle.y))

    robot_data = pygame.transform.scale(Consts.TURTLE_BOT_IMAGE, (Consts.ROBOT_WIDTH, Consts.ROBOT_HEIGHT))
    robot = pygame.Rect((robot_pixel_x, robot_pixel_y), (Consts.ROBOT_WIDTH, Consts.ROBOT_HEIGHT))
    WINDOW.blit(robot_data, (robot.x, robot.y))
    pygame.display.update()


def draw_lose_message(score):
    msg = [Consts.LOSE_MESSAGE, score]
    draw_message(msg)


def draw_message(message):
    pygame.font.init()
    background_data = pygame.transform.scale(Consts.BACKGROUND, (Consts.WINDOW_WIDTH, Consts.WINDOW_HEIGHT))
    background = pygame.Rect((0, 0), (Consts.WINDOW_WIDTH, Consts.WINDOW_HEIGHT))
    WINDOW.blit(background_data, (background.x, background.y))
    for i in range(len(message)):
        font = pygame.font.SysFont(Consts.FONT_NAME, Consts.LOSE_FONT_SIZE)
        text_img = font.render(message[i], True, Consts.LOSE_COLOR)
        WINDOW.blit(text_img, (Consts.LOSE_LOCATION[0], Consts.LOSE_LOCATION[1] + i*40))

    pygame.display.update()

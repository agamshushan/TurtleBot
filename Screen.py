import pygame
import Consts
import Trash
import TurtleBot

def index_to_pixels(x_index, y_index):
    return (x_index * 50, y_index * 100 + 100)

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

    for i in range(Consts.TURTLE_AMOUNT):
        row = trash_array[i]
        # if i % 2 != 0:
        #     row = trash_array[i][-1::-1]
        #     turtle_data = pygame.transform.scale(Consts.TURTLE_IMAGE, (
        #         Consts.TURTLE_WIDTH, Consts.TURTLE_HEIGHT))
        #     turtle = pygame.Rect(index_to_pixels(0, i),
        #                          (Consts.TURTLE_WIDTH, Consts.TURTLE_HEIGHT))
        #     WINDOW.blit(turtle_data, (turtle.x, turtle.y))


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
    draw_message(Consts.LOSE_MESSAGE + "\n" + score, Consts.LOSE_FONT_SIZE,
                 Consts.LOSE_COLOR, Consts.LOSE_LOCATION, Consts.BACKGROUND)

def draw_message(message, font_size, color, location, background_img):
    pygame.font.init()

    WINDOW.blit(background_img, (0, 0))
    font = pygame.font.SysFont(Consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    WINDOW.blit(text_img, location)

    pygame.display.update()

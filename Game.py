import Consts
import Screen
import TurtleBot
import Trash
import pygame
import time
import BeachTrash

start_time = time.time()
score = 0
# def first_stage():
#     global score
#     while BeachTrash.count_trash() > 0:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 is_run = False
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 pygame.mouse.get_pos()
#
#


def manage_game():
    global score, start_time
    is_run = True
    difficulty = Consts.START_DIFF
    Trash.init_trash_list()
    clock = pygame.time.Clock()
    while is_run:
        clock.tick(Consts.FPS)
        Trash.add_trash()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_run = False
        Screen.update_starter_screen()
        keys_pressed = pygame.key.get_pressed()
        Screen.move_robot(keys_pressed)
        score += TurtleBot.if_on_trash()
        if int(time.time() - start_time + 1) % Consts.TIME_BETWEEN_TRASH == 0:
            start_time += 1
            Trash.move_trash()
        print("0")

        is_run = Trash.has_not_eaten()
        print(is_run)
    return score


def get_score_message():
    return "Your score is: " + str(score)

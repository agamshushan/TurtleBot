import Consts
import Screen
import TurtleBot
import Trash
import pygame
import time
import BeachTrash

start_time = time.time()
score = 0
time_between_trash_moves = Consts.START_TIME_BETWEEN_TRASH


def first_stage():
    global score
    while BeachTrash.count_trash() > 0:
        pass


def second_stage():
    global score
    is_run = True
    difficulty = Consts.START_DIFF
    Trash.init_trash_list()

    while is_run:
        Screen.update_starter_screen()
        keys_pressed = pygame.key.get_pressed()
        Screen.move_robot(keys_pressed)
        score += TurtleBot.if_on_trash()
        if time.time() - start_time % time_between_trash_moves == 0:
            Trash.move_trash()
        if time.time() - start_time == Consts.TIME_BETWEEN_DIFF and \
                difficulty < Consts.MAX_DIFF:
            difficulty += 1
            change_difficulty(difficulty)
        is_run = Trash.has_not_eaten()
    return score


def change_difficulty(diff):
    global time_between_trash_moves, start_time
    if diff % 2 == 1:
        time_between_trash_moves /= 2
        start_time = time.time()
    else:
        Trash.increase_difficulty()

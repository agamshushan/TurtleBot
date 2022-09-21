import Consts
import random
import Trash

trash_beach = []


def new_beach():
    empty_beach = []
    for i in range(Consts.FIELD_MATRIX_ROWS):
        empty_beach.append([Consts.NO_OBSTACLE] * Consts.FIELD_MATRIX_COLS)

    return empty_beach


def generate_trash():
    global trash_beach
    trash_beach = new_beach()

    for i in range(Consts.NUM_OF_OBSTACLES):
        row = random.randint(0, Consts.BEACH_ROWS)
        col = random.randint(0, Consts.BEACH_COLS)
        while trash_beach[row][col] != Consts.EMPTY:
            row = random.randint(0, Consts.BEACH_ROWS)
            col = random.randint(0, Consts.BEACH_COLS)
        trash_beach[row][col] = Trash.get_random_trash()


def clean_trash(loc):
    trash_beach[loc[0]][loc[1]] = Consts.EMPTY

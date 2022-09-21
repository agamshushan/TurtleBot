import Consts
import random
import Trash

trash_beach = []


def new_beach():
    empty_beach = []
    for i in range(Consts.BEACH_ROWS):
        empty_beach.append([Consts.EMPTY] * Consts.BEACH_COLS)

    return empty_beach


def generate_trash():
    global trash_beach
    trash_beach = new_beach()

    for i in range(Consts.NUM_OF_BEACH_TRASH):
        #row = random.randint(0, Consts.BEACH_ROWS - 1)
        row = random.randint(0, 4)
        col = random.randint(0, 14)
        while trash_beach[row][col] != Consts.EMPTY:
            row = random.randint(0, Consts.BEACH_ROWS)
            col = random.randint(0, Consts.BEACH_COLS)
        trash_beach[row][col] = Trash.get_random_trash()


def clean_trash(loc):
    trash_beach[loc[0]][loc[1]] = Consts.EMPTY


def count_trash():
    count = 0
    for row in trash_beach:
        for item in row:
            count += 1 if item != Consts.EMPTY else 0
    return count


def get_trash_beach():
    return trash_beach

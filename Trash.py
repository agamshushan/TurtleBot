import Consts
import random

trash_array = [[]]
max_trash_count = 2


def init_trash_list():
    global trash_array
    for i in range(Consts.TURTLE_AMOUNT):
        for j in range(Consts.ARRAY_SIZE):
            trash_array[i][j] = Consts.TRASH_LIST[0]


def move_trash():
    global trash_array
    prev_list = trash_array
    for i in range()


def get_trash():
    return trash_array


def add_trash():
    global trash_array
    for i in trash_array:
        if count_trash_in_row(i) < max_trash_count and get_first_trash_index(i) < 3:
            trash_array[trash_array.index(i)][0] = get_random_trash()


def has_eaten():
    pass


def get_random_trash():
    return Consts.TRASH_LIST[random.randint(0, 3)]


def get_first_trash_index(row):
    for i in row:
        if i in Consts.TRASH_LIST:
            return row.index(i)


def remove_trash(index):
    trash_array[index[1]][index[0]] = Consts.TRASH_LIST[0]


def count_trash_in_row(row):
    count = 0
    for i in row:
        if i in Consts.TRASH_LIST and i != Consts.TRASH_LIST[0]:
            count += 1
    return count


def increase_difficulty():
    global max_trash_count
    max_trash_count += 1
import Consts
import random
import time

trash_array = []
max_trash_count = 2
started_time = None


def init_trash_list():
    global trash_array
    global started_time
    started_time = time.time()
    for i in range(Consts.TURTLE_AMOUNT):
            trash_array.append([Consts.EMPTY] * Consts.ARRAY_SIZE)


def move_trash():
    global trash_array

    global started_time
    curr_time = time.time()
    if curr_time - started_time >= 0.5:
        prev_list = get_trash()

        for i in range(Consts.TURTLE_AMOUNT):
            j = 0
            while j < 20:
                if prev_list[i][j] != Consts.EMPTY:
                    trash_array[i][j + 1] = prev_list[i][j]
                    prev_list[i][j] = Consts.EMPTY
                    trash_array[i][j] = Consts.EMPTY
                    j += 2
                else:
                    j += 1
        # for i in range(Consts.TURTLE_AMOUNT):
        #     for j in range(Consts.ARRAY_SIZE - 1):
        #         if prev_list[i][j] != Consts.EMPTY:
        #             trash_array[i][j + 1] = prev_list[i][j]
        #             prev_list[i][j] = Consts.EMPTY
        #             trash_array[i][j] = Consts.EMPTY

        started_time = time.time()






def get_trash():
    return trash_array


def add_trash():
    global trash_array
    for i in trash_array:
        if count_trash_in_row(i) == 0:
            trash_array[trash_array.index(i)][0] = get_random_trash()
            break
        if count_trash_in_row(i) < max_trash_count and get_first_trash_index(i) > 2:
            move_trash()
            trash_array[trash_array.index(i)][0] = get_random_trash()


def has_not_eaten():
    for i in trash_array:
        if i[Consts.ARRAY_SIZE - 1] != Consts.EMPTY:
            return False
    return True


def get_random_trash():
    return Consts.TRASH_LIST[random.randint(0, 3)]


def get_first_trash_index(row):
    for i in row:
        if i in Consts.TRASH_LIST and i != Consts.EMPTY:
            print("IN", row.index(i))
            return row.index(i)


def remove_trash(index):
    trash_array[index[1]][index[0]] = Consts.EMPTY


def count_trash_in_row(row):
    count = 0
    for i in row:
        if i != Consts.EMPTY:
            count += 1
    print(count)
    return count


def increase_difficulty():
    global max_trash_count
    max_trash_count += 1
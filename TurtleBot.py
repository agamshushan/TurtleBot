import Consts
import Trash


bot_loc = [Consts.START_X, 0]
prev_loc = [Consts.START_X, 0]


def move_soldier(direction):
    global prev_loc, bot_loc
    prev_loc = bot_loc
    if direction == Consts.UP:
        if bot_loc[1] > 0:
            bot_loc[1] = bot_loc[1] - Consts.STEP
    elif direction == Consts.DOWN:
        if bot_loc[1] < Consts.TURTLE_AMOUNT - 1:
            bot_loc[1] = bot_loc[1] + Consts.STEP
    elif direction == Consts.RIGHT:
        if bot_loc[0] < Consts.ARRAY_SIZE - 1:
            bot_loc[0] = bot_loc[0] + Consts.STEP
    elif direction == Consts.LEFT:
        if bot_loc[0] > 0:
            bot_loc[0] = bot_loc[0] - Consts.STEP


def if_on_trash():
    trash = Trash.get_trash()
    if trash[bot_loc[1]][bot_loc[0]] != Consts.EMPTY:
        Trash.remove_trash(bot_loc)


def get_loc():
    return bot_loc

def get_prev_loc():
    return prev_loc
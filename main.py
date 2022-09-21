import Consts
import Screen
import Game


def main():
    Screen.draw_message("Cleaner Bot!\nPress any key to start.")
    Screen.draw_message(Consts.INFO_CLEANER_BOT)
    Screen.draw_message((Consts.PLAY_INFO))
    score = Game.second_stage()
    print(score)
    Screen.draw_lose_message("Your score is: " + score)


if __name__ == "__main__":
    main()

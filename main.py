import Consts
import Screen
import Game


def main():
    score = Game.manage_game()
    print(score)
    Screen.draw_lose_message()


if __name__ == "__main__":
    main()

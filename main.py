import Consts
import Screen
import Game
import pygame

def wait_for_a_key():
    is_keys_pressed = False
    while not is_keys_pressed:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                is_keys_pressed = True

def main():
    Screen.draw_message(Consts.START_MESSAGE)
    wait_for_a_key()
    Screen.draw_message(Consts.INFO_CLEANER_BOT)
    wait_for_a_key()
    Screen.draw_message((Consts.PLAY_INFO))
    wait_for_a_key()
    score = Game.manage_game()
    print(score)
    Screen.draw_lose_message("Your score is: " + str(score))
    pygame.time.wait(5000)
    pygame.quit()



if __name__ == "__main__":
    main()

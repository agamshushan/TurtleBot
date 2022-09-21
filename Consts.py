import pygame
import os

TURTLE_AMOUNT = 4
ARRAY_SIZE = 21

EMPTY = 'EMPTY'
BAG = 'BAG'
CAN = 'CAN'
BOTTLE = 'BOTTLE'
TRASH_LIST = [EMPTY, BAG, CAN, BOTTLE]

# BEACH TRASH
BEACH_ROWS = 5
BEACH_COLS = 15
NUM_OF_BEACH_TRASH = 20

# TURTLE BOT:
START_X = 10

STEP = 1
UP = 'UP'
DOWN = 'DOWN'
LEFT = 'LEFT'
RIGHT = 'RIGHT'

# GAME:
TIME_BETWEEN_TRASH = 3
TIME_BETWEEN_DIFF = 5
MAX_DIFF = 6
START_DIFF = 1

# SCREEN:
FPS = 60
WINDOW_WIDTH, WINDOW_HEIGHT = 1050, 500
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

#MSG_WINDOW_WIDTH, MSG_WINDOW_HEIGHT = 500, 500
#MSG_WINDOW = pygame.display.set_mode((MSG_WINDOW_WIDTH, MSG_WINDOW_HEIGHT))

TRASH_IMAGES = {BAG: pygame.image.load(os.path.join("Bin", "bag.png")),
                BOTTLE: pygame.image.load(os.path.join("Bin", "bottle.png")),
                CAN: pygame.image.load(os.path.join("Bin", "can.png"))
                }
TURTLE_BOT_IMAGE = pygame.image.load(os.path.join("Bin", "bot.png"))
TURTLE_IMAGE = pygame.image.load(os.path.join("Bin", "turtle.png"))
BACKGROUND = pygame.image.load(os.path.join("Bin", "sea.jpeg"))
BEACH_BACKGROUND = pygame.image.load(os.path.join("Bin", "beach.jpeg"))

ROBOT_WIDTH, ROBOT_HEIGHT = 50, 100
TRASH_WIDTH, TRASH_HEIGHT = 50, 50 
TURTLE_WIDTH, TURTLE_HEIGHT = 100, 100

#messeges
WHITE = (255, 255, 255)
FONT_NAME = "Calibri"
LOSE_MESSAGE = "game over!"
LOSE_FONT_SIZE = 100  # int(0.15 * WINDOW_WIDTH)
LOSE_COLOR = WHITE
LOSE_LOCATION = (0.4 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (LOSE_FONT_SIZE / 2))

PLAY_INFO = ["Move CleanerBot with arrow or wasd keys",
                     "Clean the trash with CleanerBot before it gets to the innocent turtles",
                     "You have 3 lives."]

INFO_CLEANER_BOT = ["CleanerBot is made to clean the ocean.",
                    "Over 100,000 sea animals die from plastic pollution each year.",
                    "Every year, about 8 million tons of plastic waste escapes into the oceans from coastal nations.",
                    "If CleanerBot becomes a real thing, it will help sea life and our planet as a whole"]

import pygame
import os

pygame.init()

WIDTH,HEIGHT = 650,650
ROWS,COLUMNS = 8,8
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
ICON = pygame.image.load(os.path.join("Assets","app_icon.png")) 

BACKGROUND_IMAGE_1 = pygame.image.load(os.path.join("Assets","background.png"))
BACKGROUND_1 = pygame.transform.scale(BACKGROUND_IMAGE_1,(WIDTH,HEIGHT))

PLAY_BUTTON_ICON = pygame.image.load(os.path.join("Assets","play_button.png")) 
SETTINGS_BUTTON_ICON = pygame.image.load(os.path.join("Assets","settings_button.png"))
RETURN_BUTTON_ICON = pygame.image.load(os.path.join("Assets","left_arrow.png"))

BUTTON_ICON = pygame.image.load(os.path.join("Assets","button_text.png"))

BROWN_BOARD_ICON = pygame.image.load(os.path.join("Assets","chess_board_brown.png"))
BLACK_BOARD_ICON = pygame.image.load(os.path.join("Assets","chess_board_black.png"))
GREEN_BOARD_ICON = pygame.image.load(os.path.join("Assets","chess_board_green.png"))
BLUE_BOARD_ICON = pygame.image.load(os.path.join("Assets","chess_board_blue.png"))

BROWN_BOARD = [(179,135,91),(245,215,176),(51,31,6)] #Dark Brown - Light Brown
BLACK_BOARD = [(41,41,41),(245,245,245),(20,20,20)] #Black - White
GREEN_BOARD = [(119,150,77),(228,237,216),(64,82,39)] #Dark Green - Light Green 
BLUE_BOARD = [(121,141,189),(245,248,255),(42,55,94)] #Dark Blue - Light Blue 

DOOR_ICON = pygame.image.load(os.path.join("Assets","door.png"))
HAZARD_ICON = pygame.image.load(os.path.join("Assets","exclamation_mark.png"))

BOARD_WIDTH,BOARD_HEIGHT = 60,60
X_PADDING = 85
Y_PADDING = 85

BLACK = (0,0,0)
RED = (207,21,0)
LIGHT_RED = (168,72,56)
ORANGE = (255,147,5)
LIGHT_BROWN = (161,120,85)

#font from: https://fonts.google.com/
ORELEGAONE_FONT = "OrelegaOne-Regular.ttf"
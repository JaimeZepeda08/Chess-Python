import pygame
import os
import copy 
import math
import time 
import numpy as np
import pandas as pd 
from variables import *
from game import *
from chessAI import *
from Pieces import *
from Button import *
from HelperFunctions import *

pygame.init()

class Rules():
  def __init__(self,players,doors,hazard,board_color):
    self.players = players
    self.board_color = board_color
    self.doors = doors
    self.hazard = hazard
    self.hazard_board = CreateBoard() # <--Placeholder

rules = Rules(2,False,False,BROWN_BOARD) # <--Default rules

class Message():
  def __init__(self,text,color,size,x,y,font=ORELEGAONE_FONT):
    self.text = text
    self.color = color
    self.size = size
    self.x = x
    self.y = y
    self.font = font 

  def update_message(self,new_text,new_color,new_size,new_x,new_y,new_font=ORELEGAONE_FONT):
    self.text = new_text
    self.color = new_color
    self.size = new_size
    self.font = new_font
    self.x = new_x
    self.y = new_y

  def reset_message(self): 
    self.text = ""
    self.color = BLACK
    self.size = 32
    self.x = 0
    self.y = 0
    self.font = ORELEGAONE_FONT

#-----------Text-----------
message = Message("",LIGHT_BROWN,32,0,0)
player_1_text = Message("",BLACK,32,0,0)
player_2_text = Message("",BLACK,32,0,0)
#-----------Text-----------

#-----------Buttons-----------
play_button = Button((0,0,0),255,(WIDTH/2) - 50,(HEIGHT/2) + 20,100,100) 
settings_button = Button((0,0,0),255,(WIDTH/2) - 50,(HEIGHT/2) + 140,100,100)
return_button = Button((0,0,0),255,35,35,50,50)

player_1_button = Button((0,0,0),255,60,125,250,(int(200*0.40)))
player_2_button = Button((0,0,0),255,340,125,250,(int(200*0.40)))
curr_player_selection = Button((0,0,0),100,player_2_button.x_pos,player_2_button.y_pos,player_2_button.width,player_2_button.heigth)

door_button = Button((0,0,0),255,110,250,150,150)
door_rule_selected = Button((0,0,0),0,door_button.x_pos,door_button.y_pos,door_button.width,door_button.heigth)
door_info = Button((0,0,0),255,door_button.x_pos + door_button.width - 20,door_button.y_pos + door_button.heigth - 20,30,30)
hazard_button = Button((0,0,0),255,380,250,150,150)
hazard_rule_selected = Button((0,0,0),0,hazard_button.x_pos,hazard_button.y_pos,hazard_button.width,hazard_button.heigth)

brown_board_button = Button((0,0,0),255,55,450,125,125)
black_board_button = Button((0,0,0),255,190,450,125,125)
green_board_button = Button((0,0,0),255,325,450,125,125)
blue_board_button = Button((0,0,0),255,460,450,125,125)
curr_board = Button((0,0,0),100,brown_board_button.x_pos,brown_board_button.y_pos,brown_board_button.width,brown_board_button.heigth)
#-----------Buttons-----------

def main_menu(): 
  pygame.display.set_caption("Chess")
  WINDOW.blit(BACKGROUND_1,(0,0))
  play_button.draw_button_image(WINDOW,PLAY_BUTTON_ICON)
  settings_button.draw_button_image(WINDOW,SETTINGS_BUTTON_ICON)
  board = CreateBoard()
  if rules.doors == True: 
    SetDoors(board)
  if rules.hazard == True:
    rules.hazard_board = CreateBoard()
  pygame.display.update()
  for event in pygame.event.get():
    pos = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
      if play_button.isOver(pos):
        run = True
        while run:
          x = game_loop(board)
          if x == "main_menu":
            reset_alpha_color()
            message.reset_message()
            run = False
          elif x == "quit":
            run = False
            return "quit"
      if settings_button.isOver(pos):
        run = True
        while run:
          x = settings()
          if x == "main_menu":
            run = False
            player_1_text.reset_message()
            player_2_text.reset_message()
          elif x == "quit":
            run = False
            return "quit"
    if event.type == pygame.QUIT:
      return "quit"

def settings():
  pygame.display.set_caption("Chess - Settings")
  WINDOW.blit(BACKGROUND_1,(0,0))
  return_button.draw_button_image(WINDOW,RETURN_BUTTON_ICON)
  player_1_button.draw_button_image(WINDOW,BUTTON_ICON)
  player_1_text.update_message("1 Player",BLACK,32,player_1_button.x_pos + 60,player_1_button.y_pos + 25)
  player_2_button.draw_button_image(WINDOW,BUTTON_ICON)
  player_2_text.update_message("2 Players",BLACK,32,player_2_button.x_pos + 60,player_2_button.y_pos + 25)
  door_button.draw_button_image(WINDOW,DOOR_ICON)
  hazard_button.draw_button_image(WINDOW,HAZARD_ICON)
  brown_board_button.draw_button_image(WINDOW,BROWN_BOARD_ICON)
  black_board_button.draw_button_image(WINDOW,BLACK_BOARD_ICON)
  green_board_button.draw_button_image(WINDOW,GREEN_BOARD_ICON)
  blue_board_button.draw_button_image(WINDOW,BLUE_BOARD_ICON)
  for event in pygame.event.get():
    pos = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
      if return_button.isOver(pos):
        return "main_menu"
      if player_1_button.isOver(pos):
        rules.players = 1
        curr_player_selection.x_pos = player_1_button.x_pos
        curr_player_selection.y_pos = player_1_button.y_pos
        rules.doors = False
        door_rule_selected.change_alpha(0)
        rules.hazard = False
        hazard_rule_selected.change_alpha(0)
      if player_2_button.isOver(pos):
        rules.players = 2
        curr_player_selection.x_pos = player_2_button.x_pos
        curr_player_selection.y_pos = player_2_button.y_pos
      if door_button.isOver(pos):
        if rules.players == 2:
          rules.doors = not rules.doors
        if rules.doors == True:
          door_rule_selected.change_alpha(100)
        else:
          door_rule_selected.change_alpha(0)
      if hazard_button.isOver(pos):
        if rules.players == 2:
          rules.hazard = not rules.hazard
        if rules.hazard == True:
          hazard_rule_selected.change_alpha(100)
        else:
          hazard_rule_selected.change_alpha(0)
      if brown_board_button.isOver(pos):
        rules.board_color = BROWN_BOARD
        curr_board.x_pos = brown_board_button.x_pos
        curr_board.y_pos = brown_board_button.y_pos
      if black_board_button.isOver(pos):
        rules.board_color = BLACK_BOARD
        curr_board.x_pos = black_board_button.x_pos
        curr_board.y_pos = black_board_button.y_pos
      if green_board_button.isOver(pos):
        rules.board_color = GREEN_BOARD
        curr_board.x_pos = green_board_button.x_pos
        curr_board.y_pos = green_board_button.y_pos
      if blue_board_button.isOver(pos):
        rules.board_color = BLUE_BOARD
        curr_board.x_pos = blue_board_button.x_pos
        curr_board.y_pos = blue_board_button.y_pos
    if event.type == pygame.QUIT:
      return "quit"
  display_message(player_1_text)
  display_message(player_2_text)
  curr_player_selection.draw_button(WINDOW)
  door_rule_selected.draw_button(WINDOW)
  hazard_rule_selected.draw_button(WINDOW)
  curr_board.draw_button(WINDOW)
  pygame.display.update()

def draw_board(color):
  board_border_height,board_border_width = (BOARD_WIDTH * COLUMNS) + 10,(BOARD_HEIGHT * ROWS) + 10
  pygame.draw.rect(WINDOW,color[2],pygame.Rect(80,80,board_border_width,board_border_height))
  for n in range(ROWS):
    for i in range(COLUMNS):
      x = X_PADDING + (i * BOARD_WIDTH)
      y = Y_PADDING  + (n * BOARD_HEIGHT)
      if n % 2 == 0:
        if i % 2 == 0:
          pygame.draw.rect(WINDOW,color[1],pygame.Rect(x,y,BOARD_WIDTH,BOARD_HEIGHT))
        else:
          pygame.draw.rect(WINDOW,color[0],pygame.Rect(x,y,BOARD_WIDTH,BOARD_HEIGHT))
      else:
        if i % 2 == 0:
          pygame.draw.rect(WINDOW,color[0],pygame.Rect(x,y,BOARD_WIDTH,BOARD_HEIGHT))
        else:
          pygame.draw.rect(WINDOW,color[1],pygame.Rect(x,y,BOARD_WIDTH,BOARD_HEIGHT))

def draw_button_board():
  index = 0
  for n in range(ROWS):
    for i in range(COLUMNS):
      x = X_PADDING + (i * BOARD_WIDTH)
      y = Y_PADDING  + (n * BOARD_HEIGHT)
      button_list[index].x_pos = x
      button_list[index].y_pos = y
      button_list[index].width = BOARD_WIDTH
      button_list[index].heigth = BOARD_HEIGHT
      button_list[index].draw_button(WINDOW)
      index += 1

def draw_pieces(board):
  for n in range(ROWS):
    for i in range(COLUMNS): 
      x = X_PADDING + (i * BOARD_WIDTH)
      y = Y_PADDING  + (n * BOARD_HEIGHT)
      if board.loc[str(n + 1),numToLetter(i + 1)] != u'\u25a0' and board.loc[str(n + 1),numToLetter(i + 1)] != "D":
        icon_image = pygame.image.load(getPiece(board.loc[str(n + 1),numToLetter(i + 1)]).icon)
        icon = pygame.transform.scale(icon_image,(BOARD_WIDTH,BOARD_HEIGHT))
        WINDOW.blit(icon,(x,y))
      if rules.doors == True:
        if board.loc[str(n + 1),numToLetter(i + 1)] == "D":
          door_icon = pygame.transform.scale(DOOR_ICON,(BOARD_WIDTH,BOARD_HEIGHT))
          WINDOW.blit(door_icon,(x,y))
      if rules.hazard == True:
        if rules.hazard_board.loc[str(n + 1),numToLetter(i + 1)] == "!":
          hazard_icon = pygame.transform.scale(HAZARD_ICON,(BOARD_WIDTH,BOARD_HEIGHT))
          WINDOW.blit(hazard_icon,(x,y))

def select_piece(new_color): #also checks for events inside the game loop
  for event in pygame.event.get():
    pos = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN:
      if return_button.isOver(pos):
        return "main_menu"
      for i in button_list:
        if i.isOver(pos):
          i.change_alpha(100)
          i.change_color(new_color)
          return (i.coordinate)
    if event.type == pygame.QUIT: 
      return "quit"

def display_message(message_name): 
  font = pygame.font.Font(os.path.join("Assets",message_name.font),message_name.size)
  WINDOW.blit(font.render(message_name.text,0,message_name.color),(message_name.x,message_name.y))

def update_game_window(board):
  WINDOW.blit(BACKGROUND_1,(0,0))
  draw_board(rules.board_color)
  draw_pieces(board)
  draw_button_board()
  return_button.draw_button_image(WINDOW,RETURN_BUTTON_ICON)
  display_message(message)
  pygame.display.update()
  
def turn(curr_pos,new_pos,team,board):
  test_board = copy.deepcopy(board)
  curr_pos_list = split(curr_pos)
  selected_piece = board.loc[curr_pos_list[1],curr_pos_list[0].upper()]
  if selected_piece == u'\u25a0' or selected_piece == "D":
    message.update_message("Select a " + team + " piece",LIGHT_BROWN,32,180,580)
    reset_alpha_color()
    update_game_window(board)
    pass_coordinate(team,board)
  elif (getPiece(selected_piece).team) == team:
    if rules.doors == True and UseDoor(curr_pos,new_pos,getPiece(selected_piece).type,getPiece(selected_piece).team,board) == True:
      SetDoors(board)
    elif rules.doors == True and UseDoor(curr_pos,new_pos,getPiece(selected_piece).type,getPiece(selected_piece).team,board) == "check":
      message.update_message("Check",LIGHT_RED,32,280,580) 
      reset_alpha_color()
      update_game_window(board)
      pass_coordinate(team,board)
    else:
      if Castling(curr_pos,new_pos,team,board) == False:
        if CheckMovement(curr_pos,new_pos,getPiece(selected_piece).type,getPiece(selected_piece).team,board):
          if CheckPath(curr_pos,new_pos,board):
            if CheckNewPos(new_pos,getPiece(selected_piece).team,board):
              Move(curr_pos,new_pos,test_board)
              if Check(team,test_board):  
                message.update_message("Check",LIGHT_RED,32,280,580) 
                reset_alpha_color()
                update_game_window(board)
                pass_coordinate(team,board)
              else:
                Move(curr_pos,new_pos,board)
                PawnPromotion(new_pos,getPiece(selected_piece).type,getPiece(selected_piece).team,board)
                message.reset_message()
            else:
              message.update_message("Select another position",LIGHT_BROWN,32,160,580)
              reset_alpha_color()
              update_game_window(board)
              pass_coordinate(team,board)
          else:
            message.update_message("Select another position",LIGHT_BROWN,32,160,580)
            reset_alpha_color()
            update_game_window(board)
            pass_coordinate(team,board)
        else:
          message.update_message("Select another position",LIGHT_BROWN,32,160,580)
          reset_alpha_color()
          update_game_window(board)
          pass_coordinate(team,board)
  else:
    message.update_message("Select a " + team + " piece",LIGHT_BROWN,32,180,580)
    reset_alpha_color()
    update_game_window(board)
    pass_coordinate(team,board)

def pass_coordinate(team,board): 
  curr_pos = ""
  new_pos = ""
  reset_alpha_color()
  while curr_pos == None or curr_pos == "":
    curr_pos = select_piece(RED)
    if curr_pos == "main_menu" or curr_pos == "quit":
      return curr_pos
      break
    else:
      if curr_pos != None and curr_pos != "":
        update_game_window(board)
        while new_pos == None or new_pos == "":
          new_pos = select_piece(ORANGE)
          if new_pos == "main_menu" or new_pos == "quit":
            return new_pos
            break
          else:
            if new_pos != None and new_pos != "":
              turn(curr_pos,new_pos,team,board)

def game_loop(board):
  run = True
  game_over = False
  while run:
    update_game_window(board)
    if rules.players == 2:
      pygame.display.set_caption("Chess - White")
    if Check("white",board):
      message.update_message("Check",LIGHT_RED,32,280,580) 
      update_game_window(board)
      if Checkmate("white",board):
        message.update_message("Checkmate",LIGHT_RED,32,250,580) 
        update_game_window(board)
        game_over = True
        run = False
        break
    if game_over == False:
      if rules.doors == True:
        ResetDoors(board)
      if rules.hazard == True:
        rules.hazard_board = SetHazard("white",board)
        update_game_window(board)
      x = pass_coordinate("white",board)
      if rules.hazard == True:
        Hazard(rules.hazard_board,board)
      if x == "main_menu" or x == "quit":
        run = False
        return x
        break
    update_game_window(board)
    if rules.players == 2:
      pygame.display.set_caption("Chess - Black")
    if Check("black",board):
      message.update_message("Check",LIGHT_RED,32,280,580) 
      update_game_window(board)
      if Checkmate("black",board):
        message.update_message("Checkmate",LIGHT_RED,32,250,580) 
        update_game_window(board)
        game_over = True
        run = False
        break
    if game_over == False:
      if rules.players == 2:
        if rules.doors == True:
          ResetDoors(board)
        if rules.hazard == True:
          rules.hazard_board = SetHazard("black",board)
          update_game_window(board)
        i = pass_coordinate("black",board)
        if rules.hazard == True:
          Hazard(rules.hazard_board,board)
        if i == "main_menu" or i == "quit":
          run = False
          return i
          break
      elif rules.players == 1:
        start_time = time.time()
        AI_move = minimax(board,1,-math.inf,math.inf,True,"black") #use 1 for depth (anything greater takes too long)
        board = AI_move[1][random.randint(0,len(AI_move[1]) - 1)]
        elapsed_time = time.time() - start_time
        print("Elapsed time: " + str(elapsed_time))
        print ("board evaluation: " + str( AI_move[0]))
        message.reset_message()
        reset_alpha_color()
        update_game_window(board)
  if game_over:
    print (board) 
    pygame.time.delay(3000)
    reset_alpha_color()
    update_game_window(board)
    return "main_menu" 

def main():
  pygame.display.set_caption("Chess")
  pygame.display.set_icon((ICON))
  run = True
  while run:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
    if main_menu() == "quit":
      run = False
  pygame.quit()

if __name__ == "__main__":
  main()

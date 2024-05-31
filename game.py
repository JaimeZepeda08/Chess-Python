import numpy as np 
import pandas as pd 
import copy 
import random 
from variables import *
from Pieces import *
from Button import *
from HelperFunctions import *

def CreateBoard():
  board_values = np.zeros(64).reshape(8,8)
  rows = ["1","2","3","4","5","6","7","8"]
  columns = ["A","B","C","D","E","F","G","H"]
  new_board = pd.DataFrame(board_values,rows,columns)
  new_board[:] = u'\u25a0' 
  black_pieces_array = np.array(['bR','bKn','bB','bQ','bK','bB','bKn','bR','bP','bP','bP','bP','bP','bP','bP','bP']).reshape(2,8)
  white_pieces_array = np.array(['wP','wP','wP','wP','wP','wP','wP','wP','wR','wKn','wB','wQ','wK','wB','wKn','wR']).reshape(2,8)
  new_board.loc[["1","2"]] = black_pieces_array
  new_board.loc[["7","8"]] = white_pieces_array
  return (new_board)

def Move(curr_pos,new_pos,input_board):
  curr_pos_list = split(curr_pos)
  new_pos_list = split(new_pos)
  selected_piece = input_board.loc[curr_pos_list[1],curr_pos_list[0].upper()]
  input_board.loc[curr_pos_list[1],curr_pos_list[0].upper()] = u'\u25a0'
  input_board.loc[new_pos_list[1],new_pos_list[0].upper()] = selected_piece

def CheckMovement(curr_pos,new_pos,piece_type,piece_team,input_board):
  if piece_type == "rook":
    if slope(curr_pos,new_pos) == "undefined" or slope(curr_pos,new_pos) == 0:
      return True
    else:
      return False
  elif piece_type == "knight": 
    if (slope(curr_pos,new_pos) == 0.5 or slope(curr_pos,new_pos) == -0.5 or slope(curr_pos,new_pos) == 2 or slope(curr_pos,new_pos) == -2) and (distance(curr_pos,new_pos) >= 2.2 and distance(curr_pos,new_pos) <= 2.5):
      return True
    else:
      return False
  elif piece_type == "bishop":
    if slope(curr_pos,new_pos) == 1 or slope(curr_pos,new_pos) == -1:
      return True
    else:
      return False
  elif piece_type == "queen":
    if slope(curr_pos,new_pos) == "undefined" or slope(curr_pos,new_pos) == 0 or slope(curr_pos,new_pos) == 1 or slope(curr_pos,new_pos) == -1:
      return True
    else:
      return False
  elif piece_type == "king":
    if (slope(curr_pos,new_pos) == "undefined" or slope(curr_pos,new_pos) == 0 or slope(curr_pos,new_pos) == 1 or slope(curr_pos,new_pos) == -1) and ((distance(curr_pos,new_pos) >= 1.3 and distance(curr_pos,new_pos) <= 1.5) or (distance(curr_pos,new_pos) == 1.0)):
      return True
    else:
      return False
  elif piece_type == "pawn":
    if slope(curr_pos,new_pos) == "undefined":
      if ((piece_team == "white") and (split(curr_pos)[1] > split(new_pos)[1])) or ((piece_team == "black") and (split(curr_pos)[1] < split(new_pos)[1])):
        if input_board.loc[new_pos[1],new_pos[0].upper()] == u'\u25a0' or input_board.loc[new_pos[1],new_pos[0].upper()] == "D":
          if distance(curr_pos,new_pos) == 1.0:
            return True
          elif distance(curr_pos,new_pos) == 2.0: 
            if piece_team == "white" and split(curr_pos)[1] == "7":
              return True
            elif piece_team == "black" and split(curr_pos)[1] == "2":
              return True
            else:
              return False
          else:
            return False
        else:
          return False
      else:
        return False
    elif (slope(curr_pos,new_pos) == 1 or slope(curr_pos,new_pos) == -1) and ((distance(curr_pos,new_pos) >= 1.3 and distance(curr_pos,new_pos) <= 1.5)):
      if ((piece_team == "white") and (split(curr_pos)[1] > split(new_pos)[1])) or ((piece_team == "black") and (split(curr_pos)[1] < split(new_pos)[1])):
        if (input_board.loc[new_pos[1],new_pos[0].upper()] != u'\u25a0') and (input_board.loc[new_pos[1],new_pos[0].upper()] != "D") and (getPiece(input_board.loc[new_pos[1],new_pos[0].upper()]).team != piece_team):
          return True
    else:
      return False

def CheckNewPos(new_pos,piece_team,input_board):
  new_pos_list = split(new_pos)
  new_pos_board = input_board.loc[new_pos_list[1],new_pos_list[0].upper()]
  if (new_pos_board == u'\u25a0') or (new_pos_board == "D") or (getPiece(new_pos_board).team != piece_team):
    return True
  elif getPiece(new_pos_board).team == piece_team:
    return False

def CreatePathList(curr_pos,new_pos,input_board):
  curr_pos_list = split(curr_pos)
  new_pos_list = split(new_pos)
  path_list = []
  if (abs(int(curr_pos_list[1]) - int(new_pos_list[1])) <= 1) and (abs(letterToNum(curr_pos_list[0]) - letterToNum(new_pos_list[0])) <= 1):
    path_list.append(u'\u25a0')
    return path_list
  else:
    if slope(curr_pos,new_pos) == "undefined":
      index = 0
      if int(curr_pos_list[1]) > int(new_pos_list[1]):
        index = int(curr_pos_list[1]) - int(new_pos_list[1])
        for x in range(index - 1):
          path_list.append(input_board.loc[str((int(new_pos_list[1]) + 1) + x),new_pos_list[0].upper()])
      elif int(new_pos_list[1]) > int(curr_pos_list[1]):
        index = int(new_pos_list[1]) - int(curr_pos_list[1])
        for x in range(index - 1):
          path_list.append(input_board.loc[str((int(curr_pos_list[1]) + 1) + x),new_pos_list[0].upper()])
      return path_list
    elif slope(curr_pos,new_pos) == 0:
      index = 0
      if letterToNum(curr_pos_list[0]) > letterToNum(new_pos_list[0]):
        index = letterToNum(curr_pos_list[0]) - letterToNum(new_pos_list[0])
        for x in range(index - 1):
          path_list.append(input_board.loc[new_pos_list[1],numToLetter((letterToNum(new_pos_list[0]) + 1) + x)])
      elif letterToNum(new_pos_list[0]) > letterToNum(curr_pos_list[0]):
        index = letterToNum(new_pos_list[0]) - letterToNum(curr_pos_list[0])
        for x in range(index - 1):
          path_list.append(input_board.loc[new_pos_list[1],numToLetter((letterToNum(curr_pos_list[0]) + 1) + x)])
      return path_list
    elif slope(curr_pos,new_pos) == 1.0:
      index = 0
      if int(new_pos_list[1]) > int(curr_pos_list[1]):
        index = int(new_pos_list[1]) - int(curr_pos_list[1])
        for x in range(index - 1):
          path_list.append(input_board.loc[str((int(curr_pos_list[1]) + 1) + x),numToLetter((letterToNum(curr_pos_list[0]) + 1) + x)])
      elif int(curr_pos_list[1]) > int(new_pos_list[1]):
        index = int(curr_pos_list[1]) - int(new_pos_list[1])
        for x in range(index - 1):
          path_list.append(input_board.loc[str((int(new_pos_list[1]) + 1) + x),numToLetter((letterToNum(new_pos_list[0]) + 1) + x)])
      return path_list
    elif slope(curr_pos,new_pos) == -1.0: 
      index = 0
      if int(new_pos_list[1]) > int(curr_pos_list[1]):
        index = int(new_pos_list[1]) - int(curr_pos_list[1])
        for x in range(index - 1):
          path_list.append(input_board.loc[str((int(new_pos_list[1]) - 1) - x),numToLetter((letterToNum(new_pos_list[0]) + 1) + x)])
      elif int(curr_pos_list[1]) > int(new_pos_list[1]):
        index = int(curr_pos_list[1]) - int(new_pos_list[1])
        for x in range(index - 1):
          path_list.append(input_board.loc[str((int(curr_pos_list[1]) - 1) - x),numToLetter((letterToNum(curr_pos_list[0]) + 1) + x)])
      return path_list

def CheckPath(curr_pos,new_pos,input_board):
  path_list = CreatePathList(curr_pos,new_pos,input_board)
  curr_pos_list = split(curr_pos)
  new_pos_list = split(new_pos)
  if getPiece(input_board.loc[curr_pos_list[1],curr_pos_list[0].upper()]).type == "knight":
    return (True)
  else:
    for x in path_list:
      if x != u'\u25a0' and x != "D":
        return (False)
    return (True)

def PawnPromotion(new_pos,piece_type,piece_team,input_board):
  new_pos_list = split(new_pos)
  if piece_team == "white" and piece_type == "pawn":
    if int(new_pos_list[1]) == 1:
      new_piece = input("Select a new piece: \n1. rook \n2. knight \n3. bishop \n4. queen \n--> ")
      if new_piece == "rook" or new_piece == "Rook" or new_piece == "ROOK":
        input_board.loc[split(new_pos)[1],split(new_pos)[0].upper()] = "wR"
      elif new_piece == "knight" or new_piece == "Knight" or new_piece == "KNIGHT":
        input_board.loc[split(new_pos)[1],split(new_pos)[0].upper()] = "wKn"
      elif new_piece == "bishop" or new_piece == "Bishop" or new_piece == "BISHOP":
        input_board.loc[split(new_pos)[1],split(new_pos)[0].upper()] = "wB"
      elif new_piece == "queen" or new_piece == "Queen" or new_piece == "QUEEN":
        input_board.loc[split(new_pos)[1],split(new_pos)[0].upper()] = "wQ"
      else:
        print ("Please enter the name")
        PawnPromotion(new_pos,piece_type,piece_team,input_board)
  elif piece_team == "black" and piece_type == "pawn":
    if int(new_pos_list[1]) == 8:
      new_piece = input("Select a new piece: \n1. rook \n2. knight \n3. bishop \n4. queen \n--> ")
      if new_piece == "rook" or new_piece == "Rook" or new_piece == "ROOK":
        input_board.loc[split(new_pos)[1],split(new_pos)[0].upper()] = "bR"
      elif new_piece == "knight" or new_piece == "Knight" or new_piece == "KNIGHT":
        input_board.loc[split(new_pos)[1],split(new_pos)[0].upper()] = "bKn"
      elif new_piece == "bishop" or new_piece == "Bishop" or new_piece == "BISHOP":
        input_board.loc[split(new_pos)[1],split(new_pos)[0].upper()] = "bB"
      elif new_piece == "queen" or new_piece == "Queen" or new_piece == "QUEEN":
        input_board.loc[split(new_pos)[1],split(new_pos)[0].upper()] = "bQ"
      else:
        print ("Please enter the name")
        PawnPromotion(new_pos,piece_type,piece_team,input_board)

def Castling(curr_pos,new_pos,piece_team,input_board): 
  if getPiece(input_board.loc[split(curr_pos)[1],split(curr_pos)[0]]).type == "king":  
    if slope(curr_pos,new_pos) == 0:
      if piece_team == "white" and curr_pos == "E8":
        if new_pos == "G8" and input_board.loc["8","F"] == u'\u25a0' and input_board.loc["8","G"] == u'\u25a0' and input_board.loc["8","H"] != u'\u25a0' and getPiece(input_board.loc["8","H"]).type == "rook":
          Move(curr_pos,new_pos,input_board)
          Move("H8","F8",input_board)
          return True
        elif new_pos == "C8" and input_board.loc["8","B"] == u'\u25a0' and input_board.loc["8","C"] == u'\u25a0' and input_board.loc["8","D"] == u'\u25a0' and input_board.loc["8","A"] != u'\u25a0' and getPiece(input_board.loc["8","A"]).type == "rook":
          Move(curr_pos,new_pos,input_board)
          Move("A8","D8",input_board)
          return True
        else:
          return False
      elif piece_team == "black" and curr_pos == "E1": 
        if new_pos == "G1" and input_board.loc["1","F"] == u'\u25a0' and input_board.loc["1","G"] == u'\u25a0' and input_board.loc["1","H"] != u'\u25a0' and getPiece(input_board.loc["1","H"]).type == "rook":
          Move(curr_pos,new_pos,input_board)
          Move("H1","F1",input_board)
          return True
        elif new_pos == "C1" and input_board.loc["1","B"] == u'\u25a0' and input_board.loc["1","C"] == u'\u25a0' and input_board.loc["1","D"] == u'\u25a0' and input_board.loc["1","A"] != u'\u25a0' and getPiece(input_board.loc["1","A"]).type == "rook":
          Move(curr_pos,new_pos,input_board)
          Move("A1","D1",input_board)
          return True
        else:
          return False
      else: 
        return False
    else:
      return False
  else:
    return False

def IsUnderAttack(team,pos,input_board):
  opposite_team = ""
  if team == "white":
    opposite_team = "black"
  elif team == "black":
    opposite_team = "white"
  for n in range(ROWS):
    for i in range(COLUMNS):
      if input_board.loc[str(n + 1),numToLetter(i + 1)] != u'\u25a0':
        if getPiece(input_board.loc[str(n + 1),numToLetter(i + 1)]).team == opposite_team:
          curr_pos = numToLetter(i + 1) + str(n + 1)
          piece_type = getPiece(input_board.loc[str(n + 1),numToLetter(i + 1)]).type 
          if CheckMovement(curr_pos,pos,piece_type,opposite_team,input_board):
            if CheckPath(curr_pos,pos,input_board):
              return True

def GetPossibleMoves(team,input_board):
  possible_moves =[]
  for n in range(ROWS):
    for i in range(COLUMNS):
      if input_board.loc[str(n + 1),numToLetter(i + 1)] != u'\u25a0' and input_board.loc[str(n + 1),numToLetter(i + 1)] != "D":
        if getPiece(input_board.loc[str(n + 1),numToLetter(i + 1)]).team == team:
          selected_piece = numToLetter(i + 1) + str(n + 1)
          for x in range(ROWS):
            for y in range(COLUMNS):
              test_board = copy.deepcopy(input_board)
              castling_board = copy.deepcopy(test_board)
              check_board = copy.deepcopy(test_board)
              new_pos = numToLetter(y + 1) + str(x + 1)
              piece_type = getPiece(input_board.loc[str(n + 1),numToLetter(i + 1)]).type 
              if Castling(selected_piece,new_pos,team,castling_board):
                possible_moves.append(castling_board)
              if CheckNewPos(new_pos,team,test_board):
                if CheckMovement(selected_piece,new_pos,piece_type,team,test_board):
                  if CheckPath(selected_piece,new_pos,test_board):
                    Move(selected_piece,new_pos,check_board)
                    if Check(team,check_board) != True:
                      Move(selected_piece,new_pos,test_board)
                      possible_moves.append(test_board)
  return possible_moves

def GetKingPos(team,input_board):
  for n in range(ROWS):
    for i in range(COLUMNS):
      if input_board.loc[str(n + 1),numToLetter(i + 1)] != u'\u25a0' and input_board.loc[str(n + 1),numToLetter(i + 1)] != "D":
        if getPiece(input_board.loc[str(n + 1),numToLetter(i + 1)]).team == team and getPiece(input_board.loc[str(n + 1),numToLetter(i + 1)]).type == "king":
          return numToLetter(i + 1) + str(n + 1)

def Check(team,input_board): 
  opposite_team = ""
  if team == "white":
    opposite_team = "black"
  elif team == "black":
    opposite_team = "white"
  for n in range(ROWS):
    for i in range(COLUMNS):
      if input_board.loc[str(n + 1),numToLetter(i + 1)] != u'\u25a0' and input_board.loc[str(n + 1),numToLetter(i + 1)] != "D":
        if getPiece(input_board.loc[str(n + 1),numToLetter(i + 1)]).team == opposite_team:
          curr_pos = numToLetter(i + 1) + str(n + 1)
          king_pos = GetKingPos(team,input_board)
          piece_type = getPiece(input_board.loc[str(n + 1),numToLetter(i + 1)]).type 
          if CheckMovement(curr_pos,king_pos,piece_type,opposite_team,input_board):
            if CheckPath(curr_pos,king_pos,input_board):
              return True
 
def Checkmate(team,input_board):
  possible_moves = GetPossibleMoves(team,input_board)
  if len(possible_moves) == 0:
    return True 
  else:
    return False

def SetDoors(input_board): 
  possible_x_pos = [1,2,3,4,5,6,7,8]
  possible_y_pos = [3,4,5,6]
  random_x1 = random.choice(possible_x_pos)
  possible_x_pos.remove(random_x1)
  random_y1 = random.choice(possible_y_pos)
  possible_y_pos.remove(random_y1)
  random_x2 = random.choice(possible_x_pos)
  possible_x_pos.remove(random_x2)
  random_y2 = random.choice(possible_y_pos)
  possible_y_pos.remove(random_y2)
  if input_board.loc[str(random_y1),numToLetter(random_x1)] == u'\u25a0' and input_board.loc[str(random_y2),numToLetter(random_x2)] == u'\u25a0': 
    input_board.loc[str(random_y1),numToLetter(random_x1)] = "D"
    input_board.loc[str(random_y2),numToLetter(random_x2)] = "D"
  else:
    SetDoors(input_board)

def UseDoor(curr_pos,new_pos,piece_type,team,input_board): 
  new_pos_list = split(new_pos)
  test_board = copy.deepcopy(input_board)
  if CheckMovement(curr_pos,new_pos,piece_type,team,input_board):
    if CheckPath(curr_pos,new_pos,input_board):
      if input_board.loc[new_pos_list[1],new_pos_list[0].upper()] == "D":
        for n in range(ROWS):
          for i in range(COLUMNS):
            x = (X_PADDING + (i * BOARD_WIDTH)) + 1
            y = (Y_PADDING  + (n * BOARD_HEIGHT)) + 1
            if (n + 1) != int(new_pos_list[1]) or (i + 1) != letterToNum(new_pos_list[0]):
              if input_board.loc[str(n + 1),numToLetter(i + 1)] == "D":
                secondDoor_pos = numToLetter(i + 1) + str(n + 1)
                Move(curr_pos,secondDoor_pos,test_board)
                if Check(team,test_board):  
                    return "check"
                else:
                  input_board.loc[new_pos_list[1],new_pos_list[0].upper()] = u'\u25a0'
                  Move(curr_pos,secondDoor_pos,input_board)
                  for i in button_list: 
                    if i.isOver((x,y)):
                      i.change_alpha(100)
                      i.change_color(ORANGE)
                  return True
  return False

def ResetDoors(input_board): #in case there are less than 2 doors 
  doors = 0
  for n in range(ROWS):
    for i in range(COLUMNS):
      if input_board.loc[str(n + 1),numToLetter(i + 1)] == "D":
        doors += 1
  if doors < 2:
    for n in range(ROWS):
      for i in range(COLUMNS):
        if input_board.loc[str(n + 1),numToLetter(i + 1)] == "D":
          input_board.loc[str(n + 1),numToLetter(i + 1)] = u'\u25a0'
    SetDoors(input_board)

def SetHazard(team,input_board):
  board_values = np.zeros(64).reshape(8,8)
  rows = ["1","2","3","4","5","6","7","8"]
  columns = ["A","B","C","D","E","F","G","H"]
  hazard_board = pd.DataFrame(board_values,rows,columns)
  possible_x_pos = [1,2,3,4,5,6,7,8]
  possible_y_pos = [3,4,5,6]
  random_x1 = random.choice(possible_x_pos)
  random_y1 = random.choice(possible_y_pos)
  if input_board.loc[str(random_y1),numToLetter(random_x1)] == u'\u25a0':
    hazard_board.loc[str(random_y1),numToLetter(random_x1)] = "!"
    return hazard_board
  elif input_board.loc[str(random_y1),numToLetter(random_x1)] != "D":
    if getPiece(input_board.loc[str(random_y1),numToLetter(random_x1)]).team == team:
      if getPiece(input_board.loc[str(random_y1),numToLetter(random_x1)]).type != "king":
        hazard_board.loc[str(random_y1),numToLetter(random_x1)] = "!"
        return hazard_board
    else:
      return SetHazard(team,input_board)
  else:
    return SetHazard(team,input_board)

def Hazard(hazard_board,input_board):
  for n in range(ROWS):
    for i in range(COLUMNS):
      if hazard_board.loc[str(n + 1),numToLetter(i + 1)] == "!":
        input_board.loc[str(n + 1),numToLetter(i + 1)] = u'\u25a0'
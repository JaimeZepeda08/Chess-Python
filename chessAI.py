import numpy as np 
import pandas as pd 
import random
import math
from main import *
from game import *
from variables import *
from Pieces import *
from HelperFunctions import *

rows = ["1","2","3","4","5","6","7","8"]
columns = ["A","B","C","D","E","F","G","H"]
#values for the following lists from: https://www.freecodecamp.org/news/simple-chess-ai-step-by-step-1d55a9266977/
knight_values = np.array([-5,-4,-3,-3,-3,-3,-4,-5,-4,-2,0,0,0,0,-2,-4,-3,0,1,1.5,1.5,1,0,-3,-3,0.5,1.5,2,2,1.5,0.5,-3,-3,0.5,1.5,2,2,1.5,0.5,-3,-3,0,1,1.5,1.5,1,0,-3,-4,-2,0,0,0,0,-2,-4,-5,-4,-3,-3,-3,-3,-4,-5]).reshape(8,8)
pawn_values = np.array([0,0,0,0,0,0,0,0,0.5,1,1,-2,-2,1,1,0.5,0.5,-0.5,-1,0,0,-1,-0.5,0.5,0,0,0,2,2,0,0,0,0.5,0.5,1,2.5,2.5,1,0.5,0.5,1,1,2,3,3,2,1,1,5,5,5,5,5,5,5,5,0,0,0,0,0,0,0,0]).reshape(8,8)
rook_values = np.array([0,0,0,0.5,0.5,0,0,0,-0.5,0,0,0,0,0,0,-0.5,-0.5,0,0,0,0,0,0,-0.5,-0.5,0,0,0,0,0,0,-0.5,-0.5,0,0,0,0,0,0,-0.5,-0.5,0,0,0,0,0,0,-0.5,0.5,1,1,1,1,1,1,0.5,0,0,0,0,0,0,0,0]).reshape(8,8)
bishop_values = np.array([-2,-1,-1,-1,-1,-1,-1,-2,-1,0.5,0,0,0,0,0.5,-1,-1,1,1,1,1,1,1,-1,-1,0,1,1,1,1,0,-1,-1,0.5,0.5,1,1,0.5,0.5,-1,-1,0,0.5,1,1,0.5,0,-1,-1,0,0,0,0,0,0,-1,-2,-1,-1,-1,-1,-1,-1,-2]).reshape(8,8)
queen_values = np.array([-2,-1,-1,-0.5,-0.5,-1,-1,-2,-1,0,0.5,0,0,0,0,-1,-1,0.5,0.5,0.5,0.5,0.5,0,-1,0,0,0.5,0.5,0.5,0.5,0,-0.5,-0.5,0,0.5,0.5,0.5,0.5,0,-0.5,-1,0,0.5,0.5,0.5,0.5,0,-1,-1,0,0,0,0,0,0,-1,-2,-1,-1,-0.5,-0.5,-1,-1,-2]).reshape(8,8)
king_values = np.array([2,3,5,0,0,1,5,2,2,2,0,0,0,0,2,2,-1,-2,-2,-2,-2,-2,-2,-1,-2,-3,-3,-4,-4,-3,-3,-2,-3,-4,-4,-5,-5,-4,-4,-3,-3,-4,-4,-5,-5,-4,-4,-3,-3,-4,-4,-5,-5,-4,-4,-3,-3,-4,-4,-5,-5,-4,-4,-3]).reshape(8,8)
knight_df = pd.DataFrame(knight_values,rows,columns)
pawn_df = pd.DataFrame(pawn_values,rows,columns)
rook_df = pd.DataFrame(rook_values,rows,columns)
bishop_df = pd.DataFrame(bishop_values,rows,columns)
queen_df = pd.DataFrame(queen_values,rows,columns)
king_df = pd.DataFrame(king_values,rows,columns)

def evaluate_board(input_board,team,AI): 
  opposite_team = ""
  if team == "white":
    opposite_team = "black"
  elif team == "black":
    opposite_team = "white"
  score = 0
  for n in range(8):
    for i in range(8):
      board_row = str(n + 1)
      board_column = numToLetter(i + 1)
      pos = numToLetter(i + 1) + str(n + 1)
      if input_board.loc[board_row,board_column] != u'\u25a0':
        if getPiece(input_board.loc[board_row,board_column]).team == team:
          if getPiece(input_board.loc[board_row,board_column]).team == team:
            if getPiece(input_board.loc[board_row,board_column]).type == "pawn":
              score += 10 
              if AI:
                score += pawn_df.loc[board_row,board_column]
                if IsUnderAttack(team,pos,input_board):
                  score -= 15
            elif getPiece(input_board.loc[board_row,board_column]).type == "knight":
              score += 30
              if AI:
                score += knight_df.loc[board_row,board_column]
                if IsUnderAttack(team,pos,input_board):
                  score -= 50
            elif getPiece(input_board.loc[board_row,board_column]).type == "bishop":
              score += 30 
              if AI:
                score += bishop_df.loc[board_row,board_column]
                if IsUnderAttack(team,pos,input_board):
                  score -= 50
            elif getPiece(input_board.loc[board_row,board_column]).type == "rook":
              score += 50
              if AI:
                score += rook_df.loc[board_row,board_column]
                if IsUnderAttack(team,pos,input_board):
                  score -= 70
            elif getPiece(input_board.loc[board_row,board_column]).type == "queen":
              score += 90
              if AI:
                score += queen_df.loc[board_row,board_column]
                if IsUnderAttack(team,pos,input_board):
                  score -= 150
            elif getPiece(input_board.loc[board_row,board_column]).type == "king":
              score += 900
              if AI:
                score += king_df.loc[board_row,board_column]
                if IsUnderAttack(team,pos,input_board):
                  score -= 900
  if Check(opposite_team,input_board) and AI:
    score += 15 
    if Checkmate(opposite_team,input_board) and AI:
      score += 10000
  return score 

def evaluate(input_board,maximizing_team):
  if maximizing_team == "white":
    return evaluate_board(input_board,"white",True) - evaluate_board(input_board,"black",False)
  else:
    return evaluate_board(input_board,"black",True) - evaluate_board(input_board,"white",False)

#modified version of minimax function from: https://www.youtube.com/watch?v=-ivz8yJ4l4E
def minimax(input_board,depth,alpha,beta,maximizing_player,maximizing_team): 
  if depth == 0: 
    return evaluate(input_board,maximizing_team),None
  possible_moves = GetPossibleMoves(maximizing_team,input_board)
  best_moves = []

  if maximizing_player:
    max_eval = -math.inf
    for move in possible_moves:
      curr_eval = minimax(move,depth - 1,alpha,beta,False,maximizing_team)[0]
      if curr_eval > max_eval:
        max_eval = curr_eval
        best_moves.clear()
        best_moves.append(move)
      elif curr_eval == max_eval:
        best_moves.append(move)
      alpha = max(alpha,curr_eval)
      if beta <= alpha:
        break
    return max_eval,best_moves 

  else:
    min_eval = math.inf
    for move in possible_moves:
      curr_eval = minimax(move,depth - 1,alpha,beta,True,maximizing_team)[0]
      if curr_eval < min_eval:
        min_eval = curr_eval
        best_moves.clear()
        best_moves.append(move)
      elif curr_eval == min_eval:
        best_moves.append(move)
      beta = min(beta,curr_eval)
      if beta <= alpha:
        break
    return min_eval,best_moves 
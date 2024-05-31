import os

class Pieces():
	def __init__(self,team,type,tag,icon):
		self.team = team 
		self.type =type 
		self.tag = tag
		self.icon = icon

#White Pieces		
wR = Pieces("white","rook","wR",(os.path.join("Assets","rook_white.png")))	
wKn = Pieces("white","knight","wKn",(os.path.join("Assets","knight_white.png")))	
wB = Pieces("white","bishop","wB",(os.path.join("Assets","bishop_white.png")))	
wQ = Pieces("white","queen","wQ",(os.path.join("Assets","queen_white.png")))	
wK = Pieces("white","king","wK",(os.path.join("Assets","king_white.png")))
wP = Pieces("white","pawn","wP",(os.path.join("Assets","pawn_white.png")))	
white_pieces = [wR,wKn,wB,wQ,wK,wP]	

#Black Pieces
bR = Pieces("black","rook","bR",(os.path.join("Assets","rook_black.png")))
bKn = Pieces("black","knight","bKn",(os.path.join("Assets","knight_black.png")))
bB = Pieces("black","bishop","bB",(os.path.join("Assets","bishop_black.png")))
bQ = Pieces("black","queen","bQ",(os.path.join("Assets","queen_black.png")))	
bK = Pieces("black","king","bK",(os.path.join("Assets","king_black.png")))
bP = Pieces("black","pawn","bP",(os.path.join("Assets","pawn_black.png")))	
black_pieces = [bR,bKn,bB,bQ,bK,bP]

def getPiece(tag):
	for i in white_pieces:
	  if i.tag == tag:
	    return i
	for i in black_pieces:
	  if i.tag == tag:
	    return i
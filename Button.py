import pygame 

#Button class from: https://www.youtube.com/watch?v=4_9twnEduFA
class Button():
	def __init__(self,color,alpha,x_pos,y_pos,width,heigth,coordinate=None):
		self.color = color
		self.alpha = alpha
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.width = width
		self.heigth = heigth
		self.coordinate = coordinate

	def draw_button(self,surface): #https://stackoverflow.com/questions/6339057/draw-a-transparent-rectangle-in-pygame
		tile = pygame.Surface((self.width,self.heigth))
		tile.set_alpha(self.alpha)
		tile.fill((self.color))
		surface.blit(tile,(self.x_pos,self.y_pos))

	def draw_button_image(self,surface,image):
		button = pygame.transform.scale(image,(self.width,self.heigth))
		button.set_alpha(self.alpha)
		surface.blit(button,(self.x_pos,self.y_pos))

	def change_alpha(self,new_alpha):
		self.alpha = new_alpha

	def change_color(self,new_color):
		self.color = new_color

	def isOver(self,pos):
		if pos[0] > self.x_pos and pos[0] < self.x_pos + self.width:
			if pos[1] > self.y_pos and pos[1] < self.y_pos + self.heigth:
				return True 
		return False

def reset_alpha_color():
	for i in button_list:
	    i.change_alpha(0)
	    i.change_color((0,0,0))

A1 = Button((0,0,0),0,0,0,0,0,"A1")
A2 = Button((0,0,0),0,0,0,0,0,"A2")
A2 = Button((0,0,0),0,0,0,0,0,"A2")
A3 = Button((0,0,0),0,0,0,0,0,"A3")
A4 = Button((0,0,0),0,0,0,0,0,"A4")
A5 = Button((0,0,0),0,0,0,0,0,"A5")
A6 = Button((0,0,0),0,0,0,0,0,"A6")
A7 = Button((0,0,0),0,0,0,0,0,"A7")
A8 = Button((0,0,0),0,0,0,0,0,"A8")
B1 = Button((0,0,0),0,0,0,0,0,"B1")
B2 = Button((0,0,0),0,0,0,0,0,"B2")
B3 = Button((0,0,0),0,0,0,0,0,"B3")
B4 = Button((0,0,0),0,0,0,0,0,"B4")
B5 = Button((0,0,0),0,0,0,0,0,"B5")
B6 = Button((0,0,0),0,0,0,0,0,"B6")
B7 = Button((0,0,0),0,0,0,0,0,"B7")
B8 = Button((0,0,0),0,0,0,0,0,"B8")
C1 = Button((0,0,0),0,0,0,0,0,"C1")
C2 = Button((0,0,0),0,0,0,0,0,"C2")
C3 = Button((0,0,0),0,0,0,0,0,"C3")
C4 = Button((0,0,0),0,0,0,0,0,"C4")
C5 = Button((0,0,0),0,0,0,0,0,"C5")
C6 = Button((0,0,0),0,0,0,0,0,"C6")
C7 = Button((0,0,0),0,0,0,0,0,"C7")
C8 = Button((0,0,0),0,0,0,0,0,"C8")
D1 = Button((0,0,0),0,0,0,0,0,"D1")
D2 = Button((0,0,0),0,0,0,0,0,"D2")
D3 = Button((0,0,0),0,0,0,0,0,"D3")
D4 = Button((0,0,0),0,0,0,0,0,"D4")
D5 = Button((0,0,0),0,0,0,0,0,"D5")
D6 = Button((0,0,0),0,0,0,0,0,"D6")
D7 = Button((0,0,0),0,0,0,0,0,"D7")
D8 = Button((0,0,0),0,0,0,0,0,"D8")
E1 = Button((0,0,0),0,0,0,0,0,"E1")
E2 = Button((0,0,0),0,0,0,0,0,"E2")
E3 = Button((0,0,0),0,0,0,0,0,"E3")
E4 = Button((0,0,0),0,0,0,0,0,"E4")
E5 = Button((0,0,0),0,0,0,0,0,"E5")
E6 = Button((0,0,0),0,0,0,0,0,"E6")
E7 = Button((0,0,0),0,0,0,0,0,"E7")
E8 = Button((0,0,0),0,0,0,0,0,"E8")
F1 = Button((0,0,0),0,0,0,0,0,"F1")
F2 = Button((0,0,0),0,0,0,0,0,"F2")
F3 = Button((0,0,0),0,0,0,0,0,"F3")
F4 = Button((0,0,0),0,0,0,0,0,"F4")
F5 = Button((0,0,0),0,0,0,0,0,"F5")
F6 = Button((0,0,0),0,0,0,0,0,"F6")
F7 = Button((0,0,0),0,0,0,0,0,"F7")
F8 = Button((0,0,0),0,0,0,0,0,"F8")
G1 = Button((0,0,0),0,0,0,0,0,"G1")
G2 = Button((0,0,0),0,0,0,0,0,"G2")
G3 = Button((0,0,0),0,0,0,0,0,"G3")
G4 = Button((0,0,0),0,0,0,0,0,"G4")
G5 = Button((0,0,0),0,0,0,0,0,"G5")
G6 = Button((0,0,0),0,0,0,0,0,"G6")
G7 = Button((0,0,0),0,0,0,0,0,"G7")
G8 = Button((0,0,0),0,0,0,0,0,"G8")
H1 = Button((0,0,0),0,0,0,0,0,"H1")
H2 = Button((0,0,0),0,0,0,0,0,"H2")
H3 = Button((0,0,0),0,0,0,0,0,"H3")
H4 = Button((0,0,0),0,0,0,0,0,"H4")
H5 = Button((0,0,0),0,0,0,0,0,"H5")
H6 = Button((0,0,0),0,0,0,0,0,"H6")
H7 = Button((0,0,0),0,0,0,0,0,"H7")
H8 = Button((0,0,0),0,0,0,0,0,"H8")

button_list = [A1,B1,C1,D1,E1,F1,G1,H1,A2,B2,C2,D2,E2,F2,G2,H2,A3,B3,C3,D3,E3,F3,G3,H3,A4,B4,C4,D4,E4,F4,G4,H4,A5,B5,C5,D5,E5,F5,G5,H5,A6,B6,C6,D6,E6,F6,G6,H6,A7,B7,C7,D7,E7,F7,G7,H7,A8,B8,C8,D8,E8,F8,G8,H8]







import math

def split(word): 
	char_lst = []
	for x in word:
		char_lst.append(x)
	return char_lst

def letterToNum(letter):
	if letter.upper() == "A":
		return 1
	elif letter.upper() == "B":
		return 2
	elif letter.upper() == "C":
		return 3
	elif letter.upper() == "D":
		return 4
	elif letter.upper() == "E":
		return 5
	elif letter.upper() == "F":
		return 6
	elif letter.upper() == "G":
		return 7
	elif letter.upper() == "H":
		return 8
  
def numToLetter(num):
  if num == 1:
    return "A"
  elif num == 2:
    return "B"
  elif num == 3:
    return "C"
  elif num == 4:
    return "D"
  elif num == 5:
    return "E"
  elif num == 6:
    return "F"
  elif num == 7:
    return "G"
  elif num == 8:
    return "H"

def slope(coordinate_1,coordinate_2):
	#item [0] of list = x-axis (letters)
	#item [1] of list = y-axis (numbers)
	coordinate_1_list = split(coordinate_1)
	coordinate_2_list = split(coordinate_2)
	coordinate_1_list[0] = letterToNum(coordinate_1_list[0])
	coordinate_2_list[0] = letterToNum(coordinate_2_list[0])
	if (coordinate_1_list[0] == coordinate_2_list[0]):
		return ("undefined")
	else:
		slope = ((float(coordinate_2_list[1]) - float(coordinate_1_list[1]))/(float(coordinate_2_list[0]) - float(coordinate_1_list[0])))
		return (slope)

def distance(coordinate_1,coordinate_2):
	#item [0] of list = x-axis (letters)
	#item [1] of list = y-axis (numbers)
	coordinate_1_list = split(coordinate_1)
	coordinate_2_list = split(coordinate_2)
	coordinate_1_list[0] = letterToNum(coordinate_1_list[0])
	coordinate_2_list[0] = letterToNum(coordinate_2_list[0])
	d = math.sqrt(pow((float(coordinate_2_list[0]) - float(coordinate_1_list[0])),2) + pow((float(coordinate_2_list[1]) - float(coordinate_1_list[1])),2))
	return (d)
import sys
import random
import time

symbol = "*" * 19 
move = {}
winner = False
player1 = 'x'
player2 = '0'
r1= {1:"",2:"",3:""}
r2= {4:"",5:"",6:""}
r3= {7:"",8:"",9:""}
sentinal = 's'
global moveCount
moveCount = 0
#initiate a 2d grid with a sentinal value
grid = [[sentinal for j in range(3)]for i in range(3)]

def gridify(positions):
	i=0
	print " "	
	keylist = positions.keys()
	keylist.sort()
 	while (i < 3):
       		print symbol.rjust(23)
#		print positions
#		print "keys are: ",keylist	
		for k in keylist:
			val = positions[k]
			if k in r1:
				r1[k] = val 
			elif k in r2:
				r2[k] = val 
			elif k in r3:
				r3[k] = val 	
		if i==0: 
			gridifyVertical(r1)
		elif i==1:
			gridifyVertical(r2)
		else:
			gridifyVertical(r3)  
		i= i+1
	
def gridifyVertical(symbolpos):
	y=symbolpos.keys()
	y.sort()
	for j in y:
		print '*'.rjust(5),symbolpos[j],'*'.rjust(4),symbolpos[j+1],'*'.rjust(4),symbolpos[j+2],'*'.rjust(4)
		break
		

def letsplay():
	player1 = raw_input('Choose your Symbol, x or 0:')
	if  player1 == 'x':
		player2 = '0';
	else :
		player2 = 'x';
	print "You are" + " " +player1
	print "Computer is" + " " +  player2
	while not winner:
		playerMove()
		computerMove()	

def playerMove():
	pos = int(raw_input('Enter a position from 1-9 :'))
	if pos in move:
		print "This Position is already taken Input another"
		playerMove()
	else:
		move[pos] = player1
		gridify(move)
		print symbol.rjust(23)
		isWinner(pos)

def computerMove():
	comp_pos = random.randrange(1,9,1)
	if comp_pos not in move:
		print "Computer Plays"
		move[comp_pos] = player2
		time.sleep(2)
		gridify(move)
		print symbol.rjust(23)
		isWinner(comp_pos)		
	else:
		computerMove()

def isWinner(last_move):
	movesplayed = move.keys()
	movesplayed.sort()
	posx=-1
	posy=-1
	
	#First Translate 1d grid to 2d array for easy determination of winner	
	for x in movesplayed:
		set = False
		ctr = 0		
		for i in range(3):
			if set:
				break
			for j in range(3):
				ctr = ctr + 1
				if x == ctr:
						grid[i][j] = move[x]
						if x == last_move:
									posx = i
									posy = j							
						set = True
						break
	print "Grid is:"	
	detWinner(posx,posy,move[last_move])

def detWinner(x,y,last):
		global moveCount
		moveCount = moveCount + 1
		#check column
		for i in range(3):
			if grid[x][i] != last:
						break
			if(i == 2):
				print "Winner is " + " " + whoIs(last)	
				winner = True
		                sys.exit()
			#check row	
		for i in range(3):
			if grid[i][y] != last:
						break
			if(i==2):
				print "Winner is" + " " +  whoIs(last)
				winner = True
				sys.exit()	
			#condition that we are on diagonal
		if x==y:
			for i in range(3):
				if grid[i][i] != last:
							break
				if(i==2):
					print "Winner is" + " " + whoIs(last)
					winner = True
					sys.exit()
			#condition that we are on anti diagonal
		for i in range(3):
				if grid[i][2-i] != last:
							break
				if(i==2):
					print "Winner is " + " " + whoIs(last)
					winner = True
					sys.exit()
		if (moveCount == 8 ):
					print "Its a Draw"
					sys.exit()


def whoIs(last):
	if last == player1:
		return player1
	else:
		return player2
									
gridify(move)
print symbol.rjust(23)
letsplay()

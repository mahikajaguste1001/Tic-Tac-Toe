board=[0]*9;

#0 means empty
#1 means X
#2 means O



def display():
	XO=["X","O"]
	for i in range(0,7,3):
		for j in range(i,i+3):
			if(board[j]==0):
				print((j+1),end=" ")
			else:
				print(XO[board[j]-1],end=" ")
			if(j!=i+2):
				print("|",end=" ")
			if(j==i+2):
				print("\n",end="")
		if(i!=6):
			print("-"*10)
	print()

def winner():
	for i in range(0,3):#column wise
		if(board[i]!=0 and board[i]==board[i+3] and board[i]==board[i+6]):
			return (board[i])
	for i in range(0,7,3):#row wise
		if(board[i]!=0 and board[i]==board[i+1] and board[i]==board[i+2]):
			return (board[i])
	if(board[0]!=0 and board[0]==board[4] and board[0]==board[8]):#diagonal
		return (board[0])
	if(board[2]!=0 and board[2]==board[4] and board[2]==board[6]):#diagonal
		return (board[2])
	return -1#no winner

def takeentry(turn):
	while(True):
		print("Player",(turn+1)," - Enter position: ",end="")
		entry=input()
		if(entry.isdigit()):
			entry=int(entry)-1#0 indexed array
			if(entry<0 or entry>8):
				print("Entry should be from 1 to 9. Re-enter.")
			else:
				if(board[entry]!=0):
					print("Position occupied. Re-enter.")
				else:
					board[entry]=turn+1
					break
		else:
			print("Invalid entry. Re-enter.")

def makeentry():
	print("Machine enters at position (to be conti.)")

def singleplayer():
	print("Player 1 uses X.\nMachine uses O")
	choice=0
	turn=0
	while(True):
		print("Enter 1 to play first.\nEnter 2 to let machine play first.\nYour choice: ",end="")
		choice=input();
		if(choice=='1' or choice=='2'):
			turn=int(choice)-1
			break
		else:
			print("Invalid choice. Re-enter.")
	if(turn==0):
		display()
	else:
		print()
	while(True):
		win=winner()
		if(win==-1):
			if 0 not in board:#all positions are filled and no winner found
				print("Game Draw")
				break
			if(turn==0):
				takeentry(turn)#take position of entry from current player
			else:
				makeentry()#machine has to enter position
			display()
			turn=1-turn#to alternate between players
		else:
			if(win==1):#we have a winner
				print("Player 1 wins!")
			else:
				print("Machine wins!")
			break
	
def multiplayer():
	print("Player 1 uses X.\nPlayer 2 uses O")
	display()
	turn=0;
	while(True):
		win=winner()
		if(win==-1):
			if 0 not in board:#all positions are filled and no winner found
				print("Game Draw")
				break
			takeentry(turn)#take position of entry from current player
			display()
			turn=1-turn#to alternate between players
		else:
			if(win==1):#we have a winner
				print("Player 1 wins!")
			else:
				print("Player 2 wins!")
			break

#beginning
def main():
	print("Welcome to Tic Tac Toe")
	#to store mode of playing
	choice=0
	while(True):
		print("Enter 1 to play against computer.\nEnter 2 to play multiplayer.\nYour choice: ",end="")
		choice=input();
		if(choice=='1' or choice=='2'):
			break
		else:
			print("Invalid choice. Re-enter.")
	print()
	if(choice=='1'):
		singleplayer()
	else:
		multiplayer()

#display()
main()



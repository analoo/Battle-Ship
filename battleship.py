'''Making a game of battle ship and for fun'''

from random import randint

def create_the_board(number): 
	board = []
	for x in range(number):
		board.append(["O"] * number)
	return board
#creates the board based on a user generated size. 

def print_board(board):
	for row in board:
		print " ".join(row)
	print "\n"
#prints the board for the user to see

def build_ships():
	ship_row = randint(0, len(board) - 1)
	ship_col = randint(0, len(board) - 1)
	coordinates = [ship_row+1, ship_col+1]
	return coordinates

def lets_play():
	print "Let's play the game!"
	print "But first.. some ground rules because rules make life fun!"
	print "The board is 5x5, first block is [1,1] last block is [5,5]"
	print "You have 5 turns to guess this right!"
	print "If you decide to be funny and guess an invalid value, I'll forgive you"
	print "If you keep using the same guess, it will count against you.. because I haven't figured out otherwise"
	print "..because relationships are about forgiveness"
	print "Any questions?"
	print "Hold them to them end!! \n" 
	print "-"*10
	turn = 0
	while (turn < 5):
		print "This is your %s turn" % (turn+1)
		guess_row = int(raw_input("Guess Row: "))
		guess_col = int(raw_input("Guess Col: "))
		guess_coordinates = [guess_row, guess_col]
		if(valid_guess(guess_coordinates) == True):
			if (guess_coordinates == coordinates):
				print "Congratulations! You sunk my battleship!"
				break
			else:
				print "You missed my battleship! \n"
				board[guess_row-1][guess_col-1] = "X"
			turn+=1
		#if(valid_guess(guess_row, guess_col, n)==True):
			#was_it_hit(guess_row, guess_col)
		print_board(board)
	else:
		print "Game Over. My Battle Ship was in %s " %coordinates		

def valid_guess(guesses):
	all_guesses = [guesses]
	if(guesses[0]<1 or guesses[0]>5) or (guesses[1] < 1 or guesses[1]>5):
		print "Oops that's not even in the Ocean. Try Again"
		return False
	#elif(board[guesses[0]][guesses[1]] == "X"):
		#print "You guessed that one already."
		#return False
	return True

	#else:
		#return True

#def was_it_hit(guess_row, guess_col):
	#if (guess_row == ship_row and guess_col == ship_col):
	#	print "Congratulations! You sunk my battleship!"
	#	turn = 4
	#else:
	#	print "You missed my battleship!"
	#	board[guess_row][guess_col] = "X"
		# Print (turn + 1) here!
	#	print_board(board)
	
n = 5
board = create_the_board(n)
coordinates = build_ships()

lets_play()

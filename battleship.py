from random import randint
from termcolor import colored, cprint
import subprocess as sp

board = []
board_size = int(raw_input("What do you want the board size to be?: "))
tmp = sp.call('clear',shell=True)
#Define the ship size and init the x and y cords for ship
ship_carrier_size = 5
ship_carrier_x = []
ship_carrier_y = []
ship_battleship_size = 4
ship_battleship_x = []
ship_battleship_y = []
ship_cruser_size = 3
ship_cruser_x = []
ship_cruser_y = []
ship_submarine_size = 3
ship_submarine_x = []  
ship_submarine_y = []
ship_destroyer_size = 2
ship_destroyer_x = []
ship_destroyer_y = []
ships_left = 5


for x in range(0, board_size):
  board.append(["O"] * board_size)

def print_board(board):
  for row in board:
    cprint (' '.join(row), 'red')

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

def setup_board():
  battleship_orintation = randint(1,2)
  carrier_orintation = randint(1,2)
  cruser_orintation = randint(1,2)
  submarine_orintation = randint(1,2)
  destroyer_orintation = randint(1,2)
  if battleship_orintation == 1:
    start_x=randint(0,board_size)
    
  
ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col
setup_board()

# Everything from here on should be in your for loop
# don't forget to properly indent!
for turn in range(4):
  print "Turn", turn + 1
  guess_row = int(raw_input("Guess Row: "))-1
  guess_col = int(raw_input("Guess Col: "))-1

  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"
    break
  else:
    if guess_row not in range(board_size) or \
      guess_col not in range(board_size):
      print "Oops, that's not even in the ocean."
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"
    if (turn == 3):
      print "Game Over"
    print_board(board)

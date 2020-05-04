# ---- Global variables---- #

# Game Board
board = ["-","-","-",
          "-","-","-",
          "-","-","-"]

# If game is still going
game_still_going = True

# Who won? Or tie?
winner = None

# Who's turn is it?
current_player = "X"

# Display board
def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])

# Play a game of tic tac toe
def play_game():
  
  # Display board
  display_board()

  # While the game is still going
  while game_still_going:

    # handle a single turn of an arbitrary player
    handle_turn(current_player)

    # Check if the game has eded
    check_if_game_over()

    # Flip to the other player
    flip_player()

  # The game has ended
  if winner == "X" or winner == "0":
    print(winner + " won.")
  elif winner == None:
    print("Tie.")
    
# Handle a single turn of an arbitary player
def handle_turn(player):
  position = input("Choose a position from 1-9: ")
  position = int(position) - 1

  board[position] = "X"
  

  display_board()


def check_if_game_over():
  check_for_winner
  check_if_tie


def check_for_winner():

  # Set up global variables
  global winner

  # check rows
  row_winner = check_rows()
  # check columns
  columns_winner = check_columns()
  # check diagnols
  diagonal_winner = check_diagnols()
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None
  return

def check_rows():
  # Set up global variables
  global game_still_going
  # Check if any of the columns have all the same value
  row_1 = board[0] == board[1] == board[2] == "-"
  row_2 = board[3] == board[4] == board[5] == "-"
  row_3 = board[6] == board[7] == board[8] == "-"
  # If any rows does have a match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_still_going = False
  # Return the winner (X or O)
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  return


def check_columns():
  # Set up global variables
  global game_still_going
  # Check if any of the columns have all the same value
  column_1 = board[0] == board[3] != board[6] == "-"
  column_2 = board[1] == board[4] != board[7] == "-"
  column_2 = board[2] == board[5] != board[8] == "-"
  # If any column does have a match, flag that there is a win
  if column_1 or column_2 or column_3:
    game_still_going = False
  # Return the winner (X or O)
  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]


def check_diagonals():
  # Set up global variables
  global game_still_going
  # Check if any of the diagonals have all the same value
  diagonal_1 = board[0] == board[4] != board[8] == "-"
  diagonal_2 = board[6] == board[4] != board[2] == "-"
  # If any diagonals does have a match, flag that there is a win
  if diagonal_1 or column_2 or column_3:
    game_still_going = False
  # Return the winner (X or O)
  if column_1:
    return board[0]
  elif column_2:
    return board[6]
  return


def check_if_tie():
  return


def flip_player():
  return


play_game()



print("Hellp worlsd")
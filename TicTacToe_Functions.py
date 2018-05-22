#Function definitions

from IPython.display import clear_output

#This function displays the current board
def display_board(board):
    print("           |          |          ")
    print("     "+board[1]+"     |     "+board[2]+"    |     "+board[3]+"     ")
    print("           |          |          ")
    print("---------------------------------")
    print("           |          |          ")
    print("     "+board[4]+"     |     "+board[5]+"    |     "+board[6]+"     ")
    print("           |          |          ")
    print("---------------------------------")
    print("           |          |          ")
    print("     "+board[7]+"     |     "+board[8]+"    |     "+board[9]+"     ")
    print("           |          |          ")

#This function determines which player gets which mark
def player_input():
    player1 = "a"
    while not player1 in ["X","O"]:
        player1 = input("Please select X or O")
    return player1

#This function places the appropriate mark at a spot on the board
def place_marker(board, marker, position):
    board[position] = marker
    pass

#This function checks to see if anyone has won the game
def win_check(board, mark):
    if board[1]==mark and board[2]==mark and board[3]==mark:
        return True
    elif board[1]==mark and board[5]==mark and board[9]==mark:
        return True
    elif board[1]==mark and board[4]==mark and board[7]==mark:
        return True
    elif board[2]==mark and board[5]==mark and board[8]==mark:
        return True
    elif board[3]==mark and board[5]==mark and board[7]==mark:
        return True
    elif board[4]==mark and board[5]==mark and board[6]==mark:
        return True
    elif board[7]==mark and board[8]==mark and board[9]==mark:
        return True
    else:
        return False
    
import random

#This function randomly picks between two values 
#and says who/which mark goes first.
def choose_first(player1,player2):
    first = 0
    first = random.randint(1,2)
    if first==1:
        print(player1+" goes first")
    elif first==2:
        print(player2+" goes first")
    return first   

#This function checks if a spot is open
def space_check(board, position):
    return board[position]==" "
    pass

#This function checks if the board is full
def full_board_check(board):
    return not " " in board
    pass

#This function allows the player to select a spot on the board
#and makes sure it is an integer between 1 and 9
def player_choice(board):
    selection = 0
    while not space_check(board,selection):
        try:
            selection = int(input("Pick a spot 1 through 9"))
        except ValueError:
            print("Your entry was invalid.")
        else:
            if selection in range(1,10):
                if space_check(board,selection):
                    return selection
                    break
                else:
                    print("That spot's already taken")
            else:
                selection = 0
                print("Your entry was invalid.")
                
#This function checks for whether the game will be replayed.                
def replay():
    again = ""
    while again not in ["Yes","y","yes","Y","No","no","N","n"]:
        again = input("Play another round?")
        if again in ["Yes","yes","Y","y"]:
            return True
        elif again in ["No","no","N","n"]:
            return False
        else:
            print("Please select yes or no")

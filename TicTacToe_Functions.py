from IPython.display import clear_output

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

def player_input():
    player1 = "a"
    while not player1 in ["X","O"]:
        player1 = input("Please select X or O")
    return player1
    
def place_marker(board, marker, position):
    board[position] = marker
    pass

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

def choose_first():
    first = 0
    first = random.randint(1,2)
    if first==1:
        print("X goes first")
    elif first ==2:
        print("O goes first")
    return first   

def space_check(board, position):
    return board[position]==" "
    pass

def full_board_check(board):
    return not " " in board
    pass

def player_choice(board):
    selection = 0
    while not space_check(board,selection):
        selection = int(input("Pick a spot 1 through 9"))
        if not type(selection) == int:
            print("Please choose a number 1 through 9")
            selection = input("Pick a spot 1 through 9")
        
        if space_check(board,selection):
            return int(selection)
            break
        else:
            print("That spot's already taken")

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

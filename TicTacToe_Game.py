print('Welcome to Tic Tac Toe!')

game = True
while game:
    #Setting the game up here
    board = ["#"," "," "," "," "," "," "," "," "," "]
    player1 = " "
    player2 = " "
    game_on = True
    first = 0
    
    #Designating players
    player1 = player_input()
    if player1 == "X":
        player2 = "O"
    elif player1 == "O":
        player2 = "X"
        
    
    print("Alright! Player 1 is "+player1+" and Player 2 is "+player2)
    first = choose_first()
    print("Time to get it on!")
    
    while game_on:
        #Player 1's turn
        if not int(first)%2==0:
            display_board(board)
            print("Player 1:")
            selection = player_choice(board)
            place_marker(board, player1, selection)
            display_board(board)
            
        #check to see if this selection wins
        if win_check(board, player1):
            print("Congratulations! You win Player 1!")
            game = replay()
            game_on = False
            break
        
        
        #check to see if the board is full
        if full_board_check(board) and game_on:
            print("It's a draw!")
            game = replay()
            game_on = False
            break
        first = first + 1
        
        #Player 2's turn
        if int(first)%2==0:
            display_board(board)
            print("Player 2:")
            selection = player_choice(board)
            place_marker(board, player2, selection)
            display_board(board)
        
        
        #check to see if this selection wins
        if win_check(board, player2):
            print("Congratulations! You win Player 1!")
            game = replay()
            game_on = False
            break
        pass
        
        #check to see if the board is full
        if full_board_check(board) and game_on:
            print("It's a draw!")
            game = replay()
            game_on = False
            break
        first = first + 1
        
        if game_on == False and game == False:
            print("Thanks for playing!")
        elif game_on == False and game == True:
            print("Let's go again!")
        
            
    

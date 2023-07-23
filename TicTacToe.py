#Game Board
def GameBoard(values):
    print('\n')
    #Row1
    print("\t    |    |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print("\t____|____|____")
    #Row2
    print("\t    |    |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print("\t____|____|____")
    #Row3
    print("\t    |    |")
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t    |    |")
    print('\n')

#Score Board
def ScoreBoard(score_board):
    print("\t-----------------------------")
    print("\t       Score Board             ")
    print("\t-----------------------------")

    players= list(score_board.keys())
    print("\t   ", players[0], "\t   ",score_board[players[0]])
    print("\t   ", players[1], "\t   ",score_board[players[1]])

    print("\t------------------------------\n")

#Check which payer has won the game
def check_winner(player_pos,curr_player):
    #winning combinations
    possibilities=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

    #Check if any player satisfied the winning condition
    for x in possibilities:
        if all(y in player_pos[curr_player] for y in x):
            return True #if satisfies the condition
    return False # if not satisfied

#Check if the game is a draw
def check_draw(player_pos):
    if len(player_pos['X'])+len(player_pos['O']) == 9:
        return True
    return False

#Each player game turn
def game_play(curr_player):
    values=['' for x in range(9)] #  this is a list of empty strings to store the positions of the player
    player_pos={'X':[], 'O':[]} #stores the positions occupied by the player
    #Game Loop
    while True:
        GameBoard(values) #prints the game board

        # try...except block for player input
        try:
            print("Player ", curr_player, "'s trun, make a move by your box choice?",end="")
            move=int(input())
        except ValueError:
            print("Wrong Input!! Try Again")
            continue
        #Check for the edge condition
        if move <1 or move > 9:
            print("please choose the right number betweeen 1 to 9")
            continue
        #Check if cell is occupied or not
        if values[move-1]!='':
            print("the position is occupied! Try Again!")
            continue

        #GameBoard Status
        values[move-1] = curr_player #updating game board
        player_pos[curr_player].append(move) #updating player positions into a list to check the winning possibility list
        #Calling check_winner 
        if check_winner(player_pos,curr_player): 
            GameBoard(values)
            print("Player ",curr_player," has won the game!")
            print('\n')
            return curr_player
        
        #calling check_draw
        if check_draw(player_pos):
            GameBoard(values)
            print("Game is Draw")
            print('\n')
            return 'D'
        
        #switching between players
        if curr_player == 'X':
            curr_player = 'O'
        else:
            curr_player= 'X'

if __name__=="__main__":
    print("Player1 Details")
    play1=input("Enter the name of the player: ")
    print('\n')
    
    print("Player 2 details")
    play2=input("Enter the name of the player: ")
    print('\n')

    #ScoreBoard details
    score_board = {play1: 0, play2: 0}
    ScoreBoard(score_board)

    curr_player= play1 #stores the player name
    player_choice={'X' : "" , 'O':""} #choices choosen by the players
    options= ['X','O']

    #Starting the game, this loop runs until either of them chooses to Quit
    while True:
        #User menu
        print("Turn to choose for", curr_player)
        print("Enter 1 for X")
        print('Enter 2 for O')
        print("Enter 3 for Quit")

        #try...except block for user choice
        try:
            choice = int(input())
        except ValueError:
            print("wrong Inout! Try Again!\ n")
            continue

        #conditions for user choice
        if choice ==1:
            player_choice['X'] = curr_player
            if curr_player == play1:
                player_choice['O']= play2
            else:
                player_choice['O'] = play1
        
        elif choice ==2:
            player_choice['O'] = curr_player
            if curr_player == play1:
                player_choice['X'] = play2
            else:
                player_choice['X'] =play1
        
        elif choice == 3:
            print("Final Scores")
            ScoreBoard(score_board)
            break
        else:
            print("Wrong Choice!! Try Again!")

        #Storing winner
        winner = game_play(options[choice-1])

        #changing the score board
        if winner!= 'D':
            player_won=player_choice[winner]
            score_board[player_won] = score_board[player_won]+1
        ScoreBoard(score_board)

        #Switching between player for a new game:
        if curr_player == play1:
            curr_player = play2
        else:
            curr_player= play1

    













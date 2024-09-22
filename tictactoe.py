# creating a simple tic-tac-to game 
user_name1=input('player1 enter your name: ') 
user_name2=input('player2 enter your name: ')
print(f'Welcome To TIC-TAC-TOE {user_name1.upper()} & {user_name2.upper()}')
board=['-','-','-',
        '-','-','-',
        '-','-','-']
game_is_still_going=True
def start_game():
    # display the game board
    def display_board():
        print(board[0]+"|"+board[1]+"|"+board[2])
        print(board[3]+"|"+board[4]+"|"+board[5])
        print(board[6]+"|"+board[7]+"|"+board[8])
    display_board()
    # move from x or o
    def choose_move():
        choose_move.user_name1_input=input(f"{user_name1} Enter your move from 'x' or 'o': ")   
        if choose_move.user_name1_input=='x':
            print(f"{user_name2} your turn 'o' ")
        else:
            print(f"{user_name2} your turn 'x' ")
    choose_move()
    # add the input to board
    def input_position():
        user_name1_input_position=int(input(f"{user_name1} Enter the position from 1 to 9: "))
        board[user_name1_input_position-1]=choose_move.user_name1_input
        display_board()
    def check_for_win():
        global game_is_still_going
        # row winner
        row1=board[0]==board[1]==board[2]!="-"
        row2=board[3]==board[4]==board[5]!="-"
        row3=board[6]==board[7]==board[8]!="-"
        # column winner
        column1=board[0]==board[1]==board[2]!="-"
        column2=board[3]==board[4]==board[5]!="-"
        column3=board[6]==board[7]==board[8]!="-"
        # diagonal winner
        diagonal1=board[0]==board[1]==board[2]!="-"
        diagonal2=board[3]==board[4]==board[5]!="-"
        diagonal3=board[6]==board[7]==board[8]!="-"
        # winner
        if row1 or row2 or row3:
            game_is_still_going=False
            if row1:
                return board[0]
            elif row2:
                return board[3]
            elif row3:
                return board[6]
        if column1 or column2 or column3:
            game_is_still_going=False
            if column1:
                return board[0]
            elif column2:
                return board[1]
            elif column3:
                return board[2]
        if diagonal1 or diagonal2 or diagonal3:
            game_is_still_going=False
            return board[4]
    def check_for_tie():
        if board!="-":
            print('Game is Tie')
    def game_result():
        check_for_win()
        check_for_tie()
    def swap_turn():
        pass

    while game_is_still_going:
        input_position()
        swap_turn()
        game_result()





start_game()


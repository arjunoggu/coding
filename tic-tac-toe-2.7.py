def bboard():
    print('| '   ' |  | '  ' |  | '  ' |')
    print(" ")
    print('| '   ' |  | '  ' |  | '  ' |')
    print(" ")
    print('| '   ' |  | '  ' |  | '  ' |')
    print(" ")
    print('Welcome to the Tic Tac Toe game!')


def display_board():
    print('| ' + board[1] + ' |  | ' + board[2] + ' |  | ' + board[3] + ' |')
    print(" ")
    print('| ' + board[4] + ' |  | ' + board[5] + ' |  | ' + board[6] + ' |')
    print(" ")
    print('| ' + board[7] + ' |  | ' + board[8] + ' |  | ' + board[9] + ' |')
    print(" ")


def human_input(mark):
    while True:
        inp = raw_input('Enter your move [1-9]:')
        if inp.isdigit():
            if int(inp) < 10 and int(inp) > 0:
                inp = int(inp)
                if board[inp] == " ":
                    return inp
                else:
                    print("Please enter a valid move")
            else:
                print("Please enter a valid move")
        else:
            print("Only integers [1-9] are allowed\nPlease enter a valid move")


def winning(mark, board):
    winning_place = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for win_place in winning_place:
        if board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == mark:
            return True


def win_move(i, board, mark):
    temp_board = list(board)
    temp_board[i] = mark
    if winning(mark, temp_board):
        return True
    else:
        return False


def cpu_input(cpu, human, board):
    for i in range(1, 10):
        if board[i] == ' ' and win_move(i, board, cpu):
            return i
    for i in range(1, 10):
        if board[i] == ' ' and win_move(i, board, human):
            return i
    for i in [5, 1, 7, 3, 2, 9, 8, 6, 4]:
        if board[i] == ' ':
            return i


def win_check(human, cpu):
    winning_place = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for win_place in winning_place:
        if board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == human:
            print('You won!!')
            return False
        elif board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == cpu:
            print('Computer won')
            return False
    if ' ' not in board:
        print('MATCH DRAW!!')
        return False
    return True


def user_choice():
    while True:
        inp = raw_input('Are you making the first move (y/n) :')
        if inp in ['y', 'Y']:
            print('Your moves are Xs')
            return 'y', 'n'
        elif inp in ['N', 'n']:
            print('Your moves are Xs')
            return 'n', 'y'
        else:
            print('Please enter either "y" or "n"')


def game():
    global board
    play = True
    board = ['', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    human, cpu = user_choice()
    human_i='X'
    cpu_i='O'
    bboard()
    while play:
        if human == 'y':
            x = human_input(human_i)
            board[x] = human_i
            display_board()
            play = win_check(human_i, cpu_i)
            if play:
                o = cpu_input(cpu_i, human_i, board)
                print('Computer made a move')
                board[o] = cpu_i
                display_board()
                play = win_check(human_i, cpu_i)
        else:
            o = cpu_input(cpu_i, human_i, board)
            print('Computer made a move')
            board[o] = cpu_i
            display_board()
            play = win_check(human_i, cpu_i)
            if play:
                x = human_input(human_i)
                board[x] = human_i
                display_board()
                play = win_check(human_i, cpu_i)


if __name__ == '__main__':
    game()
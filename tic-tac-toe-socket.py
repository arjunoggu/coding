import socket


class ServerClient:
    global board
    play = True
    board = ['', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def __init__(self):
        self.serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def bind(self):
        port = 1235
        self.serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serversock.bind(('', port))
        self.serversock.listen(5)

    def accept(self):
        (clientsocket, address) = self.serversock.accept()
        print('Got connection from', address)
        return clientsocket

    def connect(self, host, port):
        self.serversock.connect((host, port))

    def send(self, msg):
        self.serversock.send(bytes(msg))

    def receive(self):
        return self.serversock.recv(1024).decode()

    def stopApp(self):
        print("Game Ended. Thanks for playing!")
        self.serversock.close()

    def bboard(self):
        print('| '   ' |  | '  ' |  | '  ' |')
        print("")
        print('| '   ' |  | '  ' |  | '  ' |')
        print("")
        print('| '   ' |  | '  ' |  | '  ' |')
        print("")

    def display_board(self):
        print('| ' + board[1] + ' |  | ' + board[2] + ' |  | ' + board[3] + ' |')
        print("")
        print('| ' + board[4] + ' |  | ' + board[5] + ' |  | ' + board[6] + ' |')
        print("")
        print('| ' + board[7] + ' |  | ' + board[8] + ' |  | ' + board[9] + ' |')
        print("")

    def human_input(self, mark):
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

    def winning(self, mark, board):
        winning_place = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        for win_place in winning_place:
            if board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == mark:
                return True

    def win_move(self, i, board, mark):
        temp_board = list(board)
        temp_board[i] = mark
        if self.winning(mark, temp_board):
            return True
        else:
            return False

    def win_check(self, human, opponent):
        winning_place = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        for win_place in winning_place:
            if board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == human:
                print('You won!!')
                return False
            elif board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == opponent:
                print('Opponent won')
                return False
        if ' ' not in board:
            print('MATCH DRAW!!')
            return False
        return True

    def end(self):
        print("Game Ended. Thanks for playing!")


def main():
    global board
    play = True
    app = ServerClient()
    server = raw_input("Are u the server (y/n) :")
    if server == 'y':
        h1 = 'X'
        h2 = 'O'
        print('Your moves are s')
        app.bboard()
        print('Waiting for other player to connect...')
        app.bind()
        client = app.accept()
        print("Welcome to Tic Tac Toe Game!!")
        reply = 'init'
        while play:
            play = app.win_check(h1, h2)

            if play:
                x = app.human_input(h1)
                board[x] = h1
                app.display_board()
                play=app.win_check(h1,h2)
                if(play):
                    print("Waiting for opponent move")
                    x_str = str(x)
                    client.send(x_str.encode('utf-8'))
                    reply = int(client.recv(1024).decode())
                    board[reply] = h2
                    app.display_board()
                else:
                    x_str = str(x)
                    client.send(x_str.encode('utf-8'))
                    stop = '0'
                    client.send(stop.encode('utf-8'))
                    app.stopApp()


            else:
                x_str = str(x)
                client.send(x_str.encode('utf-8'))
                stop = '0'
                client.send(stop.encode('utf-8'))
                app.stopApp()
        #app.end()


    elif server == 'n':
        h1 = 'X'
        h2 = 'O'
        print('Your moves are Os')
        client = raw_input("Enter opponent name to connect to:")
        app.connect(client, 1235)
        print("Welcome to Tic Tac Toe Game!!")
        app.bboard()
        print("Waiting for opponent move:")

        reply = 'init'
        while play:

            msg = int(app.receive())
            board[msg] = h1

            if msg == 0:
                play = False
                app.stopApp()
                break
            else:

                board[msg] = h1
                app.display_board()
                o_check = app.win_check(h2, h1)
                if o_check:

                    if msg == '0':
                        reply = '0'
                        app.send(reply.encode())
                        break
                    o = app.human_input(h2)
                    board[o] = h2
                    o_str = str(o)
                    app.display_board()

                    if play:
                        app.send(o_str.encode('utf-8'))
                        print("Waiting for opponent move:")


    else:
        print('please enter valid answer')



if __name__ == '__main__':
    main()
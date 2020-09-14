#from random import randint

class Player:
    def __init__(self , name , mark):
        self.name = name
        self.mark = mark

    def __str__(self):
        return f'Name: {self.name} , Mark: {self.mark}'

    def __repr__(self):
        return f'Name: {self.name} , Mark: {self.mark}'

BOARD_SIZE = 3
game_over = False

def print_board(board):
    for row in board:
        values = []
        for cell in row:
            if cell == None:
                values.append(' ')
            else:
                values.append(cell)
        values_str = ' | '.join(values)
        print(f"| {values_str} |")

def setup_player(mark=None):
    name = input('Name: ')
    if not mark:
        mark = input('Mark: ')
        while mark not in ('X' , 'O'):
            mark = input('Mark :')
    else:
        print(f'Mark: {mark}')
    return Player(name, mark)
    #return Player(f'Player_{randint(1, 10)}' , mark)

def setup_board(size):
    return [[None] * size for _ in range(size)]

def setup():
    player_one = setup_player()
    player_two = setup_player('O' if player_one.mark == 'X' else 'X')
    board = setup_board(BOARD_SIZE)

    return (board, player_one , player_two)

def get_pos(player , board):
    pos = int(input(f'{player.name} chooses a free position from [1-9]:'))
    while not pos in range(1,10):
        pos = int(input(f'{player.name} chooses a free position from [1-9]:'))

    row = (pos - 1) // BOARD_SIZE
    col = (pos - 1) % BOARD_SIZE

    #checks if position is taken by a mark
    while board[row][col] != None:
        pos = int(input(f'{player.name} chooses a free position from [1-9]:'))
        row = (pos - 1) // BOARD_SIZE
        col = (pos - 1) % BOARD_SIZE
    return (row,col)

def choose_pos(board, player):
    (row, col) = get_pos(player , board)
    board[row][col] = player.mark

def all_single_value(ll, value):
    for v in ll:
        if v != value:
            return False
    return True

def check_game_over(board , player):
    rows = board
    row_checks = [all_single_value(row, player.mark) for row in rows]
    columns = [[board[i][j] for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]
    column_checks =[all_single_value(column , player.mark) for column in columns]
    diagonals = [[board[i][i] for i in range(BOARD_SIZE)],
                 [board[i][BOARD_SIZE - i - 1] for i in range(BOARD_SIZE)]]
    diagonal_checks = [all_single_value(diagonal , player.mark) for diagonal in diagonals]

    all_checks = [
        *row_checks,
        *column_checks,
        *diagonal_checks
    ]

    return any(all_checks)

def print_game_over(board, player):
    print_board(board)
    print(f'{player.name} won!')
    game_over = True

def game_loop(board , players):
    current_player , next_player = players
    while not game_over:
        print_board(board)
        # player chooses position
        choose_pos(board , current_player)
        #check for end of game
        if check_game_over(board, current_player):
            print_game_over(board, current_player)
        current_player , next_player = next_player , current_player

def print_welcome_screen(player):
    print('This is the numeration of the board')
    print('| 1 | 2 | 3 |')
    print('| 4 | 5 | 6 |')
    print('| 7 | 8 | 9 |')
    print(f'{player.name} starts first')

def start_game():
    (board, *players) = setup()
    print_welcome_screen(players[0])
    game_loop(board , players)

start_game()
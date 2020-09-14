def create_matrix(n):
    matrix = []
    for _ in range(n):
        line = [x for x in input()]
        matrix.append(line)

    return matrix


def is_valid(pos, size):
    pos_r = pos[0]
    pos_c = pos[1]
    return 0 <= pos_r < size and 0 <= pos_c < size


def get_killed_knights(matrix, r, c, size):
    knights_killed = 0
    rows = [-2, -1, 1, 2, 2, 1, -1, -2]
    cols = [1, 2, 2, 1, -1, -2, -2, -1]

    for i in range(8):
        current_pos = [r + rows[i], c + cols[i]]
        if is_valid(current_pos, size):
            if matrix[current_pos[0]][current_pos[1]] == 'K':
                knights_killed += 1

    return knights_killed


n = int(input())
board = create_matrix(n)
killed = 0

while True:
    to_kill = []
    most_kills = 0

    for row in range(n):
        for col in range(n):
            if board[row][col] == 'K':
                killed_knights = get_killed_knights(board, row, col, n)
                if killed_knights > most_kills:
                    most_kills = killed_knights
                    to_kill = [row, col]

    if most_kills == 0:
        break

    to_kill_row = to_kill[0]
    to_kill_col = to_kill[1]
    board[to_kill_row][to_kill_col] = '0'
    killed += 1

print(killed)

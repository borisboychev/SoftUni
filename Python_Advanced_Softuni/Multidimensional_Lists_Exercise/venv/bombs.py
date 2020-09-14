def explode(bomb_r, bomb_c, size, m):
    bomb = m[bomb_r][bomb_c]
    for row in range(bomb_r - 1, bomb_r + 2):
        for col in range(bomb_c - 1, bomb_c + 2):
            current_pos = [row, col]
            if is_valid(current_pos, size) and matrix[current_pos[0]][current_pos[1]] > 0:
                m[current_pos[0]][current_pos[1]] -= bomb


def is_valid(matrix, size):
    r = matrix[0]
    c = matrix[1]

    return 0 <= r < size and 0 <= c < size


n = int(input())
matrix = []

for _ in range(n):
    matrix.append([int(x) for x in input().split()])

bomb_nums = input().split()

for bomb in bomb_nums:
    tokens = [int(x) for x in bomb.split(',')]
    bomb_row = tokens[0]
    bomb_col = tokens[1]

    if matrix[bomb_row][bomb_col] > 0:
        explode(bomb_row, bomb_col, n, matrix)
        matrix[bomb_row][bomb_col] = 0

alive_count = 0
alive_cells_sum = 0

for row in range(n):
    for col in range(n):
        if matrix[row][col] > 0:
            alive_count += 1
            alive_cells_sum += matrix[row][col]

print(f'Alive cells: {alive_count}')
print(f'Sum: {alive_cells_sum}')

for row in matrix:
    print(' '.join([str(x) for x in row]))

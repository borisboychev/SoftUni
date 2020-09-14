import sys

def find_bunny_pos(m, n):
    for row in range(n):
        for col in range(n):
            if m[row][col] == 'B':
                return (row, col)


def create_matrix(n):
    m = []
    for _ in range(n):
        m.append(input().split())

    return m


def is_valid(x , size):
    return 0 <= x < size


n = int(input())
field = create_matrix(n)
biggest_eggs_sum = -sys.maxsize
bunny_pos = find_bunny_pos(field, n)
# print(bunny_pos)
best_dir = ''
directions = {'up': (-1, 0),
              'right': (0, 1),
              'down': (1, 0),
              'left': (0, -1)}

for direction in directions:
    current_sum = 0
    r = bunny_pos[0]
    c = bunny_pos[1]

    if not is_valid(r + directions[direction][0] , n ) or not is_valid(
            c + directions[direction][1] , n):
        continue

    while is_valid(r,n) and is_valid(c,n):
        current_cell = field[r][c]
        if current_cell != 'B' and current_cell != 'X':
                current_sum += int(current_cell)
        elif current_cell == 'X':
            break

        r += directions[direction][0]
        c += directions[direction][1]

    if current_sum > biggest_eggs_sum:
        biggest_eggs_sum = current_sum
        best_dir = direction

print(best_dir)
row = bunny_pos[0] + directions[best_dir][0]
col = bunny_pos[1] + directions[best_dir][1]

while is_valid(row, n) and is_valid(col, n):
    if field[row][col] == 'X':
        break
    print([row, col])
    row += directions[best_dir][0]
    col += directions[best_dir][1]

print(biggest_eggs_sum)

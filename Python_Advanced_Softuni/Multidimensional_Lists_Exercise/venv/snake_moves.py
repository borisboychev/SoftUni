from collections import deque


def create_matrix(*args):
    r = args[0]
    c = args[1]

    return [['' for x in range(c)] for _ in range(r)]


(rows, cols) = [int(x) for x in input().split()]
text = deque(input())
matrix = create_matrix(*(rows, cols))

for row in range(rows):
    for col in range(cols):
        current_col = col
        current_ch = text.popleft()
        if row % 2 != 0:
            # <-
            current_col = cols - 1 - col
        matrix[row][current_col] = current_ch
        text.append(current_ch)

for row in matrix:
    print(''.join([str(x) for x in row]))

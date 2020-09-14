def create_matrix(*args):
    h = args[0]
    w = args[1]
    m = []

    for _ in range(h):
        line = [int(x) for x in input().split()]
        if len(line) == w:
            m.append(line)

    return m


(height, width) = [int(x) for x in input().split()]
matrix = create_matrix(*(height, width))
biggest_sum = 0
biggest_matrix = []

for i in range(height - 2):
    for j in range(width - 2):
        current_sum = 0
        current_matrix = []
        row_counter = 0

        for r in range(i, i + 3):
            current_matrix.append([])
            for c in range(j, j + 3):
                #print(matrix[r][c])
                current_matrix[row_counter].append(matrix[r][c])
                current_sum += matrix[r][c]
            row_counter += 1

        if current_sum > biggest_sum:
            biggest_sum = current_sum
            biggest_matrix = current_matrix

print(f'Sum = {biggest_sum}')
for row in biggest_matrix:
    print(' '.join([str(x) for x in row]))

(height, width) = [int(x) for x in input().split()]

matrix = []
swapped = False

for _ in range(height):
    matrix.append([x for x in input().split()])

text_input = input().split()

while True:

    if text_input[0] == 'END':
        break

    if text_input[0] == 'swap' and len(text_input) == 5:
        r_1 = int(text_input[1])
        c_1 = int(text_input[2])
        r_2 = int(text_input[3])
        c_2 = int(text_input[4])

        if 0 <= r_1 <= width and 0 <= c_1 <= height and 0 <= r_2 <= width and 0 <= c_2 <= height:
            matrix[r_1][c_1], matrix[r_2][c_2] = matrix[r_2][c_2], matrix[r_1][c_1]
            swapped = True
            if swapped:
                for row in matrix:
                    print(' '.join([str(x) for x in row]))
                swapped = False
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')

    text_input = input().split()

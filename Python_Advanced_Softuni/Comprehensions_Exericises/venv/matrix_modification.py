n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

while True:
    token = input().split()
    if token[0] == 'END':
        break

    r = int(token[1])
    c = int(token[2])
    v = int(token[3])
    if 0 <= r < n and 0 <= c < n:
        if token[0] == 'Add':
            matrix[r][c] += v
        elif token[0] == 'Subtract':
            matrix[r][c] -= v
    else :
        print("Invalid coordinates")

[print(' '.join(str(x) for x in row)) for row in matrix]
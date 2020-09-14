n = int(input())

matrix = []
left_diagonal = 0
right_diagonal = 0

for i in range(n):
    line = [int(x) for x in input().split()]
    matrix.append(line)
    right_diagonal += matrix[i][n - i - 1]
    # print(right_diagonal)
    left_diagonal += matrix[i][i]
    # print(left_diagonal)

print(abs(left_diagonal - right_diagonal))

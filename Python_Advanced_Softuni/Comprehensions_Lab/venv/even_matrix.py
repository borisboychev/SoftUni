n = int(input())

matrix = [input().split(', ') for i in range(n)]

matrix = [[int(x) for x in row if int(x) % 2 == 0] for row in matrix]

print(matrix)
def read_matrix(n):
    return [map(int , input().split(', ')) for _ in range(n)]


n = int(input())
matrix = read_matrix(n)

flattened = [num for sublist in matrix for num in sublist]
print(flattened)
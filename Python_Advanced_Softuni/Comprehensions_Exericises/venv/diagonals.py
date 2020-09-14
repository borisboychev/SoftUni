def matrix_creator(n):
    matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]

    return matrix


def primery_diagonal(matrix , n):
    primery_diagonal = [matrix[i][i] for i in range(n)]

    return primery_diagonal


def secondary_diagonal(matrix, n):
    secondary_diagonal = [matrix[j][n - 1 - j] for j in range(n)]

    return secondary_diagonal

n = int(input())
matrix = matrix_creator(n)
print(f"First diagonal: {', '.join(str(x) for x in primery_diagonal(matrix , n))}."
      f" Sum: {sum(primery_diagonal(matrix , n))}")

print(f"Second diagonal: {', '.join(str(x) for x in secondary_diagonal(matrix , n))}."
      f" Sum: {sum(secondary_diagonal(matrix , n))}")


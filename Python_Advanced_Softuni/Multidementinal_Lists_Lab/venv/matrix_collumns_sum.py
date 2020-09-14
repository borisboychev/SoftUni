
def read_int_list(separator = ' '):
    return [int(x) for x in input().split(separator)]

(rows_count , columns_count) = read_int_list(', ')
matrix = []

for _ in range(rows_count):
    matrix.append(read_int_list())

#print(matrix)

columns_sum = [0] * columns_count

for r in range(rows_count):
    for c in range(columns_count):
        columns_sum[c] += matrix[r][c]

[print(x) for x in columns_sum]
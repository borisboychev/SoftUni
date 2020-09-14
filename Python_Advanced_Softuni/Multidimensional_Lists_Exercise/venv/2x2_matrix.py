def find_matching_pairs(matrix, width, height):
    two_by_two_found = 0
    for i in range(height - 1):
        for j in range(width - 1):
            if matrix[i][j] == matrix[i][j + 1] and matrix[i][j] == matrix[i + 1][j] and matrix[i + 1][j] == \
                    matrix[i + 1][j + 1]:
                two_by_two_found += 1

    return two_by_two_found


def print_result(found):
    if found >= 1:
        return found
    return 0


(height, width) = [int(x) for x in input().split()]
matrix = []

for _ in range(height):
    line = input().split()
    if len(line) == width:
        matrix.append(line)

pairs_found = find_matching_pairs(matrix, width, height)

print(print_result(pairs_found))

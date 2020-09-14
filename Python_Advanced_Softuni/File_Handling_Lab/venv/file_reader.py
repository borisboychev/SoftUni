def calculate_sum_with_loop(file_path):
    file  = open(file_path , 'r')
    result = 0

    for line in file:
        result += int(line)

    return result

file_path = r'nums.txt'
print(calculate_sum_with_loop(file_path))

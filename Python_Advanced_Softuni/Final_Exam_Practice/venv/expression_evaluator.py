from collections import deque
from math import floor

def handle_expression(el , temp):
    temp = [int(x) for x in temp]
    result = temp[0]
    for n in temp[1:]:
        if el == '-':
            result -= n
        elif el == '+':
            result += n
        elif el == '*':
            result *= n
        elif el == '/':
            result /= n
    return result



expression = deque(input().split())
temp_nums = []

while True:
    current_el = expression.popleft()

    if current_el in '-+/*':
        result = floor(handle_expression(current_el , temp_nums))
        expression.appendleft(str(result))
        temp_nums = []

        if len(expression) == 1:
            break
    else:
        temp_nums.append(current_el)

print(expression[0])
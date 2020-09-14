from collections import deque
from math import floor

def evaluate(sign, numbers):
    sum = int(numbers[0])
    for i in numbers[1:]:
        if sign == "+":
            sum += int(i)
        elif sign == "-":
            sum -= int(i)
        elif sign == "*":
            sum *= int(i)
        elif sign == "/":
            sum /= int(i)

    return sum


expression = deque(input().split())
numbers = []


while True:

    current = expression.popleft()
    if current in '-+*/':
        result = floor(evaluate(current , numbers))
        expression.appendleft(str(result))
        numbers = []
        if len(expression) == 1:
            break
    else:
        numbers.append(current)

print(expression[0])

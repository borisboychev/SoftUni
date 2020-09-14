def operate(operator, *args):
    result = 1
    for x in args:
        if operator == "+":
            return sum(args)
        elif operator == "*":
            result *= x
        elif operator == "/":
            result /= x
    return result

print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("/", 4, 2))
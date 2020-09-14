def sum_numbers(num1 , num2):
    return num1 + num2

def multiply_numbers(num1 , num2):
    return num1 * num2


def func_executor(*args):
    ll = []
    for i in args:
        func = i[0]
        arguments = i[1]
        ll.append(func(*arguments))

    return ll

print(func_executor((sum_numbers , (1,2)) , (multiply_numbers , (2,4))))


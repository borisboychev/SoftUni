def read_input():
    text = input()
    times = int(input())
    return (text , times)

def solve():
    try:
        (text , times) = read_input()
    except ValueError:
        return f'Value times must be an int'
    return text * times

print(solve())


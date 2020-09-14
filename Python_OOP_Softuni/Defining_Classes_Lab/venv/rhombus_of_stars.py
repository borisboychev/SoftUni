def generate_row(index, n):
    indent = ' ' * (n - index - 1)
    stars = '* ' * (index + 1)
    print(indent + stars)

def print_rhombus(n):
    for i in range(n):
        generate_row(i , n)

    for i in range(n - 2, -1 , -1):
        generate_row(i , n)

print_rhombus(int(input()))

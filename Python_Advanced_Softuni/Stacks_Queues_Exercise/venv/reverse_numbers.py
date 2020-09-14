def reverse_numbers():
    numbers = input().split()
    reversed_numbers = []
    while numbers:
        reversed_numbers.append(numbers.pop())

    return ' '.join(reversed_numbers)

print(reverse_numbers())
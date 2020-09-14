command = input()
numbers = [int(x) for x in input().split()]

if command == 'Even':
    filtered_numbers = sum(filter(lambda x: x % 2 == 0 , numbers))
else:
    filtered_numbers = sum(filter(lambda  x: x % 2 != 0 , numbers))

print(filtered_numbers * len(numbers))


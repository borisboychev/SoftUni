elements = [int(x) for x in input().split(', ')]

even_numbers = [x for x in elements if x % 2 == 0]
odd_numbers = [x for x in elements if x % 2 != 0]
positive = [x for x in elements if x >= 0]
negative = [x for x in elements if x < 0]

print(f"Positive: {', '.join(str(x) for x in positive)}")
print(f"Negative: {', '.join(str(x) for x in negative)}")
print(f"Even: {', '.join(str(x) for x in even_numbers)}")
print(f"Odd: {', '.join(str(x) for x in odd_numbers)}")


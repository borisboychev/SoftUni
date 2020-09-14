def is_valid_number(num):
    return any([num % d == 0 for d in range(2,11)])


start = int(input())
end = int(input())

print(
    [x for x in range(start , end+1) if is_valid_number(x)]
)
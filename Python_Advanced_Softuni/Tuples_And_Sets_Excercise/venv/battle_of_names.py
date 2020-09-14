n = int(input())

odd_set = set()
even_set = set()

for i in range(1 , n+1):
    name = input()
    ascii_sum = 0
    for letter in name:
        ascii_sum += ord(letter)

    if ascii_sum % 2 == 0:
        even_set.add(ascii_sum//i)
        continue
    odd_set.add(ascii_sum//i)

if sum(odd_set) == sum(even_set):
    union_values = odd_set.union(even_set)
    print(', '.join([str(x) for x in union_values]))
elif sum(odd_set) > sum(even_set):
    diff_values = odd_set.difference(even_set)
    print(', '.join([str(x) for x in diff_values]))
elif sum(even_set) > sum(odd_set):
    symetric_diff_values = odd_set.symmetric_difference(even_set)
    print(', '.join([str(x) for x in symetric_diff_values]))


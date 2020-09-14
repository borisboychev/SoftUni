(n,m) = [int(x) for x in input().split()]
loop_range = n + m
set_m = set()
set_n = set()

for _ in range(n):
    set_n.add(int(input()))

for _ in range(m):
    set_m.add(int(input()))

uniques = set_n.intersection(set_m)
[print(x) for x in (uniques)]

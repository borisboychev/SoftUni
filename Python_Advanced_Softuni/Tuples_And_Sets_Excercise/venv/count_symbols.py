string = input()
set = set()
for i in string:
    set.add(i)

ll = [x for x in set]

for j in sorted(ll):
    print(f'{j}: {string.count(j)} time/s')
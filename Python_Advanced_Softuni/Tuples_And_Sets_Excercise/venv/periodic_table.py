n = int(input())
compounds = set()

for _ in range(n):
    el = set(input().split())
    compounds = compounds.union(el)


{print(x) for x in compounds}
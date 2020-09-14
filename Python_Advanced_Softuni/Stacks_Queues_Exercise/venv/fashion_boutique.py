clothes = [int(i) for i in input().split()]
rack_capacity = int(input())
racks_needed = 0
sum = 0

while clothes:
    current = clothes.pop()
    sum += current
    if sum > rack_capacity:
        clothes.append(current)
        sum = 0
        racks_needed += 1

    elif sum == rack_capacity:
        sum = 0
        racks_needed += 1

print(racks_needed + 1)
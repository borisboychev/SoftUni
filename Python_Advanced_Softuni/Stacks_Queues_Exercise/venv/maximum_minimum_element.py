def solve():
    elements = []
    lines = int(input())
    if  1 > lines > 105:
        return

    for _ in range(lines):
        command = input().split()
        if 1 > int(command[0]) > 109:
            break

        if command[0] == '1':
            if 1 > int(command[1]) > 4:
                break
            elements.append(int(command[1]))
            continue

        if command[0] == '2':
            if elements:
                elements.pop()
            continue

        if command[0] == '3':
            if elements:
                print(max(elements))
            continue

        if command[0] == '4':
            if elements:
                print(min(elements))
            continue

    elements = [str(i) for i in elements]
    return ", ".join(elements[::-1])


print(solve())
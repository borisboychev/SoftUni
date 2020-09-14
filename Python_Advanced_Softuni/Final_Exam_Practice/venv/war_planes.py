def get_new_changes(steps, dir_chnages):
    return dir_chnages[0] * int(steps) , dir_chnages[1] * int(steps)


n = int(input())
field = []
player_pos = []
targets_count = 0
directions = {
    'up' : (-1,0),
    'right' : (0 , 1),
    'left' : (0,-1),
    'down' : (1,0)
}

for i in range(n):
    line = input().split()
    for j in range(n):
        if line[j] == 'p':
            player_pos = [i , j]
        elif line[j] == 't':
            targets_count += 1
    field.append(line)

m = int(input())
for _ in range(n):
    command = input().split()
    direction = command[1]
    steps = command[2]
    new_changes = get_new_changes(steps, directions[direction])
    if command[0] == 'shoot':
        field[shooting_pos[0]][shooting_pos[1]] = 'x'
    elif command[0] == 'move':
        pass
print(field)
def create_field(n):
    f = []
    for _ in range(n):
        f.append(input().split())

    return f


def targets_found(field, size):
    targets = 0
    for row in range(size):
        for col in range(size):
            if field[row][col] == 't':
                targets += 1

    return targets


def get_player_pos(field, size):
    for r in range(n):
        for c in range(n):
            if field[r][c] == 'p':
                # row , col
                return (r, c)


def is_valid(moved_pos, size):
    return 0 <= moved_pos[0] < size and 0 <= moved_pos[1] < size


def change_position(moved_pos, field, size):
    current_pos = get_player_pos(field, size)

    for r in range(size):
        for c in range(size):
            field[current_pos[0]][current_pos[1]] = '.'
            field[moved_pos[0]][moved_pos[1]] = 'p'

    return field


n = int(input())
field = create_field(n)
lines = int(input())

movement_directions = {'right': (0, 1),
                       'down': (1, 0),
                       'left': (0, -1),
                       'up': (-1, 0)}

shooting_directions = {'right': (0, 1),
                       'down': (1, 0),
                       'left': (0, -1),
                       'up': (-1, 0)}

max_targets = targets_found(field, n)
targets_destroyed = 0
complete = False

while True:

    for i in range(lines):
        token = input().split()
        command = token[0]

        if command == 'move':
            dir = token[1]
            steps = int(token[2])

            current_pos = get_player_pos(field, n)
            moved_pos = (current_pos[0] + movement_directions[dir][0] * steps,
                         current_pos[1] + movement_directions[dir][1] * steps)
            if is_valid(moved_pos, n):
                if field[moved_pos[0]][moved_pos[1]] == '.':
                    field = change_position(moved_pos, field, n)

        if command == 'shoot':
            dir = token[1]
            steps = int(token[2])

            current_pos = get_player_pos(field, n)
            shot_pos = (current_pos[0] + shooting_directions[dir][0] * steps,
                        current_pos[1] + shooting_directions[dir][1] * steps)

            if is_valid(shot_pos, n):
                if field[shot_pos[0]][shot_pos[1]] == 't':
                    targets_destroyed += 1
                    field[shot_pos[0]][shot_pos[1]] = 'x'
                    if max_targets - targets_destroyed <= 0:
                        complete = True
                        break
                elif field[shot_pos[0]][shot_pos[1]] == '.':
                    field[shot_pos[0]][shot_pos[1]] = 'x'

    if complete:
        print(f'Mission accomplished! All {max_targets} targets destroyed.')
        break

    if targets_found(field, n) >= 1:
        print(f'Mission Failed! {max_targets - targets_destroyed} targets left.')
        break

for row in field:
    print(' '.join([str(x) for x in row]))

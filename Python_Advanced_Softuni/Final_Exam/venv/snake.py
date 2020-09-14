def cretae_field(n):
    field = []
    for _ in range(n):
        field.append([x for x in input()])

    return field


def get_snake_pos(field, n):
    for row in range(n):
        for col in range(n):
            if field[row][col] == 'S':
                return (row, col)


def is_valid(new_pos, size):
    return 0 <= new_pos[0] < size and 0 <= new_pos[1] < size


def get_burrow(field, n):
    burrows = []
    for row in range(n):
        for col in range(n):
            if field[row][col] == 'B':
                burrows.append((row, col))

    return (burrows[0], burrows[1])


def change_pos_trough_burrow(field, n, burrow_one, burrow_two, current_pos):
    if current_pos == burrow_one:
        field[burrow_one[0]][burrow_one[1]] = '.'
        return (burrow_two[0], burrow_two[1])
    elif (current_pos) == (burrow_two):
        field[burrow_two[0]][burrow_two[1]] = '.'
        return (burrow_one[0], burrow_one[1])


def snake_movement(field, n, new_pos):
    if field[new_pos[0]][new_pos[1]] == 'B':
        burrow_one = get_burrow(field, n)[0]
        burrow_two = get_burrow(field, n)[1]

        new_burrow_pos = change_pos_trough_burrow(field, n, burrow_one, burrow_two, new_pos)
        new_pos = new_burrow_pos

    field[current_pos[0]][current_pos[1]] = '.'
    field[new_pos[0]][new_pos[1]] = 'S'


def winnin_pos(field, new_pos, directions, command):
    print(f'You won! You fed the snake.')
    field[new_pos[0]][new_pos[1]] = 'S'
    field[new_pos[0] - directions[command][0]][new_pos[1] - directions[command][1]] = '.'


n = int(input())
field = cretae_field(n)

directions = {'up': (-1, 0),
              'right': (0, 1),
              'down': (1, 0),
              'left': (0, -1)}

food_eated = 0
while True:

    command = input()
    current_pos = get_snake_pos(field, n)
    if command == 'up':
        new_pos = (current_pos[0] + directions[command][0], current_pos[1] + directions[command][1])
        if not is_valid(new_pos, n):
            print(f'Game over!')
            field[get_snake_pos(field, n)[0]][get_snake_pos(field, n)[1]] = '.'
            break
        if field[new_pos[0]][new_pos[1]] == '*':
            food_eated += 1
            if food_eated >= 10:
                winnin_pos(field, new_pos, directions, command)
                break

        snake_movement(field, n, new_pos)

    elif command == 'down':
        new_pos = (current_pos[0] + directions[command][0], current_pos[1] + directions[command][1])
        if not is_valid(new_pos, n):
            print(f'Game over!')
            field[get_snake_pos(field, n)[0]][get_snake_pos(field, n)[1]] = '.'
            break
        if field[new_pos[0]][new_pos[1]] == '*':
            food_eated += 1
            if food_eated >= 10:
                winnin_pos(field, new_pos, directions, command)
                break
        snake_movement(field, n, new_pos)

    elif command == 'left':
        new_pos = (current_pos[0] + directions[command][0], current_pos[1] + directions[command][1])
        if not is_valid(new_pos, n):
            print(f'Game over!')
            field[get_snake_pos(field, n)[0]][get_snake_pos(field, n)[1]] = '.'
            break
        if field[new_pos[0]][new_pos[1]] == '*':
            food_eated += 1
            if food_eated >= 10:
                winnin_pos(field, new_pos, directions, command)
                break
        snake_movement(field, n, new_pos)

    elif command == 'right':
        new_pos = (current_pos[0] + directions[command][0], current_pos[1] + directions[command][1])

        if not is_valid(new_pos, n):
            print(f'Game over!')
            field[get_snake_pos(field, n)[0]][get_snake_pos(field, n)[1]] = '.'
            break

        if field[new_pos[0]][new_pos[1]] == '*':
            food_eated += 1
            if food_eated >= 10:
                winnin_pos(field, new_pos, directions, command)
                break

        snake_movement(field, n, new_pos)

print(f'Food eaten: {food_eated}')
for row in field:
    print(''.join([str(x) for x in row]))

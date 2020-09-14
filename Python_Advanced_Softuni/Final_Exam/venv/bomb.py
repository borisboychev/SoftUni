from collections import deque

bomb_effects = deque([int(x) for x in input().split(', ')])
bomb_casings = [int(x) for x in input().split(', ')]
datura_bombs = 0
cherry_bombs = 0
smoke_decoy_bombs = 0
filled = False

while True:
    if not bomb_effects:
        break

    if not bomb_casings:
        break

    sum = 0
    current_effect = bomb_effects.popleft()
    current_casting = bomb_casings.pop()

    sum = current_effect + current_casting

    if sum == 40:
        datura_bombs += 1
    elif sum == 60:
        cherry_bombs += 1
    elif sum == 120:
        smoke_decoy_bombs += 1

    else:
        bomb_casings.append(current_casting-5)
        bomb_effects.appendleft(current_effect)

    if cherry_bombs >= 3 and smoke_decoy_bombs >= 3 and datura_bombs >= 3:

        print(f'Bene! You have successfully filled the bomb pouch!')
        filled = True
        break

if not filled:
    print(f"You don't have enough materials to fill the bomb pouch.")

if bomb_effects:
    print(f'Bomb Effects: {", ".join([str(x) for x in bomb_effects])}')

else:
    print(f'Bomb Effects: empty')

if bomb_casings:
    print(f'Bomb Casings: {", ".join([str(x) for x in bomb_casings])}')
else:
    print('Bomb Casings: empty')

print(f'Cherry Bombs: {cherry_bombs}')
print(f'Datura Bombs: {datura_bombs}')
print(f'Smoke Decoy Bombs: {smoke_decoy_bombs}')


from collections import deque

datura_bomb = 0
cherry_bomb = 0
smoke_decoy_bomb = 0

bomb_effects = deque(int(x) for x in input().split(', '))
bomb_casings = deque(int(x) for x in input().split(', '))

bomb_effects_empty = False
bomb_casings_empty = False

while True:
    current_bomb_effect = bomb_effects.popleft()
    current_bomb_casing = bomb_casings.pop()
    bomb_pouch = current_bomb_effect + current_bomb_casing

    if bomb_pouch == 40:
        datura_bomb += 1
    elif bomb_pouch == 60:
        cherry_bomb += 1
    elif bomb_pouch == 120:
        smoke_decoy_bomb += 1
    else:
        bomb_effects.appendleft(current_bomb_effect)
        bomb_casings.append(current_bomb_casing - 5)

    succeeded = datura_bomb >= 3 and cherry_bomb >= 3 and smoke_decoy_bomb >= 3
    if len(bomb_effects) == 0 or len(bomb_casings) == 0 or succeeded:
        if succeeded:
            print('Bene! You have successfully filled the bomb pouch!')
        else:
            print("You don't have enough materials to fill the bomb pouch.")

        if len(bomb_effects) == 0:
            bomb_effects_empty = True

        if len(bomb_casings) == 0:
            bomb_casings_empty = True

        break

if bomb_effects_empty:
    print('Bomb Effects: empty')
else:
    print(f'Bomb Effects: {", ".join([str(x) for x in bomb_effects])}')

if bomb_casings_empty:
    print('Bomb Casings: empty')
else:
    print(f'Bomb Casings: {", ".join([str(x) for x in bomb_casings])}')

print(f"Cherry Bombs: {cherry_bomb}")
print(f"Datura Bombs: {datura_bomb}")
print(f"Smoke Decoy Bombs: {smoke_decoy_bomb}")

from collections import deque

materials = deque([int(x) for x in input().split()])
magic_values = deque([int(x) for x in input().split()])

toys = {
    'Doll': 0,
    'Wooden train': 0,
    'Teddy bear': 0,
    'Bicycle': 0
}

while True:
    if not materials or not magic_values:
        break

    current_material = materials.pop()
    current_magic_value = magic_values.popleft()

    if current_material == 0 or current_magic_value == 0:
        if current_material != 0:
            materials.append(current_material)
        if current_magic_value != 0:
            magic_values.appendleft(current_magic_value)
        continue

    product = current_material * current_magic_value

    if product < 0:
        materials.append(abs(current_material + current_magic_value))
    else:
        if product == 150:
            toys['Doll'] += 1
        elif product == 250:
            toys['Wooden train'] += 1
        elif product == 300:
            toys['Teddy bear'] += 1
        elif product == 400:
            toys['Bicycle'] += 1
        else:
            materials.append(current_material + 15)

is_christmas = (toys['Doll'] >= 1 and toys['Wooden train'] >= 1) or (toys['Teddy bear'] >= 1 and toys['Bicycle'] >= 1)

if is_christmas:
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if materials:
    print(f'Materials left: {", ".join([str(x) for x in reversed(materials)])}')
if magic_values:
    print(f'Magic left: {", ".join([str(x) for x in magic_values])}')

for (k, v) in sorted(toys.items()):
    if v > 0:
        print(f'{k}: {v}')

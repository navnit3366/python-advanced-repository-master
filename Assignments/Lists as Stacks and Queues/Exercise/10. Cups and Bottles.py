from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = deque([int(x) for x in input().split()])
wasted_water = 0

while True:
    current_cup = cups[0]
    current_bottle = bottles.pop()

    if current_cup < current_bottle:
        current_bottle -= current_cup
        wasted_water += current_bottle
        cups.popleft()

    elif current_cup >= current_bottle:
        cups[0] -= current_bottle

        if cups[0] == 0:
            cups.popleft()

    if not cups:
        print(f"Bottles: {' '.join(list(map(str, bottles)))}")
        print(f"Wasted litters of water: {wasted_water}")
        break
    elif not bottles:
        print(f"Cups: {' '.join(list(map(str, cups)))}")
        print(f"Wasted litters of water: {wasted_water}")
        break

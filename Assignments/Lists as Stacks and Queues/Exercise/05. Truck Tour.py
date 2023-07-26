from collections import deque


def solve(n):
    pumps = deque()

    for _ in range(n):
        fuel, distance = list(map(int, input().split()))
        pumps.append([fuel, distance])

    for i in range(n):
        is_success = True
        total_fuel = 0
        for _ in range(n):
            current_fuel, current_distance = pumps.popleft()
            total_fuel += current_fuel - current_distance

            if total_fuel < 0:
                is_success = False
            pumps.append([current_fuel, current_distance])

        if is_success:
            print(i)
            break

        pumps.append(pumps.popleft())


solve(n=int(input()))

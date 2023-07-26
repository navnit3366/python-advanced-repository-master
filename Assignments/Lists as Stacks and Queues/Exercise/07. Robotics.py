from collections import deque


def get_robots(robots_data: list):
    for i in robots_data:
        robot = i.split("-")
        robots_available.append([robot[0], int(robot[1])])
        robots_dict[robot[0]] = int(robot[1])


def next_second(h: int, m: int, s: int):
    s += 1
    if s >= 60:
        s -= 60
        m += 1
        if m >= 60:
            m -= 60
            h += 1
            if h >= 24:
                h -= 24

    return [h, m, s]


robots_available = deque()
robots_unavailable = deque()
robots_dict = dict()
get_robots(input().split(";"))

time = list(map(int, input().split(":")))

products = deque()
while True:
    cmd = input()

    if cmd == "End":
        break

    products.append(cmd)

while products:
    product = products.popleft()
    time = next_second(time[0], time[1], time[2])

    if robots_unavailable:
        robots_length = len(robots_unavailable)
        for _ in range(robots_length):
            robot_unavailable_name, robot_unavailable_time = robots_unavailable.popleft()
            robot_unavailable_time -= 1

            if robot_unavailable_time == 0:
                robots_available.appendleft([robot_unavailable_name, robots_dict[robot_unavailable_name]])
            else:
                robots_unavailable.append([robot_unavailable_name, robot_unavailable_time])

    if robots_available:
        current_robot_name, current_robot_time = robots_available.popleft()
        print(f"{current_robot_name} - {product} [{time[0]:02d}:{time[1]:02d}:{time[2]:02d}]")

        if current_robot_time != 0:
            robots_unavailable.appendleft([current_robot_name, current_robot_time])
        else:
            robots_available.appendleft([current_robot_name, current_robot_time])

    else:
        products.append(product)

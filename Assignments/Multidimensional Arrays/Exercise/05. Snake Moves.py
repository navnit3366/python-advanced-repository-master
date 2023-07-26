n, m = list(map(int, input().split()))
snake = [x for x in input()]


last_ind = 0
for row in range(n):
    line = []
    for col in range(m):
        if last_ind >= len(snake):
            last_ind = 0
        line.append(snake[last_ind])
        last_ind += 1

    if row % 2 != 0:
        print("".join(reversed(line)))
    else:
        print("".join(line))

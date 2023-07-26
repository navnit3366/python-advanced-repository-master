from collections import deque

queue = deque()
while True:
    cmd = input()

    if cmd == "Paid":
        [print(queue.popleft()) for x in range(len(queue))]

    elif cmd == "End":
        print(f"{len(queue)} people remaining.")
        break
    else:
        queue.append(cmd)

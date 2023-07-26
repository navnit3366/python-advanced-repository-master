from collections import deque

stack = deque()
n = int(input())

for _ in range(n):
    cmd = list(map(int, input().split()))

    if cmd[0] == 1:
        stack.appendleft(cmd[1])
    elif cmd[0] == 2 and len(stack) > 0:
        stack.popleft()
    elif cmd[0] == 3 and len(stack) > 0:
        print(max(stack))
    elif cmd[0] == 4 and len(stack) > 0:
        print(min(stack))

stack = [str(x) for x in stack]
print(", ".join(stack))

data = list(input())
stack = []

for i in range(len(data)):
    stack.append(data.pop())

print("".join(stack))

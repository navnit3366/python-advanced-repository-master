numbers = list(input().split())
stack = []
[stack.append(numbers.pop()) for i in range(len(numbers))]
print(' '.join(stack))

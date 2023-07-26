line = input().split()
filtered = [x for x in line if len(x) % 2 == 0]
[print(x) for x in filtered]

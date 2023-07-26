import itertools

names = input().split(", ")
n = int(input())

for i in itertools.combinations(names, n):
    print(', '.join(i))

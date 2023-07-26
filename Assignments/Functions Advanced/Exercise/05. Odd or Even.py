cmd = input()
numbers = list(map(int, input().split()))
n = len(numbers)

commands = {
    "Odd": sum(list(filter(lambda x: x % 2 != 0, numbers))) * n,
    "Even": sum(list(filter(lambda x: x % 2 == 0, numbers))) * n
}

print(commands[cmd])

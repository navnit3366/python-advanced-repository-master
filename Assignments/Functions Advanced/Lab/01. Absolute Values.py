def absolute(*args):
    return [abs(x) for x in args[0]]


numbers = list(map(float, input().split()))
print(absolute(numbers))

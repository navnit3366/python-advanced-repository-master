def rounding(*args):
    res = [round(x) for x in args[0]]
    return res


numbers = list(map(float, input().split()))
print(rounding(numbers))
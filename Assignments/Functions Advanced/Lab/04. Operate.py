from functools import reduce


def operate(*args):
    symbol = args[0]
    numbers = args[1:]
    symbols = {
        "+": reduce(lambda a, b: a + b, numbers),
        "-": reduce(lambda a, b: a - b, numbers),
        "/": reduce(lambda a, b: a / b, numbers),
        "*": reduce(lambda a, b: a * b, numbers)
    }
    return symbols[symbol]


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))

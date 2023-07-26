def recursive_power(*args):
    number = args[0]
    power = args[1]

    if power == 2:
        return number * number

    return number * recursive_power(number, power - 1)


print(recursive_power(2, 10))
print()
print(recursive_power(10, 100))

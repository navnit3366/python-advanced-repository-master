def even_odd(*args):
    cmd = args[-1]
    numbers = args[:-1]

    if cmd == "even":
        return list(filter(lambda x: x % 2 == 0, numbers))
    else:
        return list(filter(lambda x: x % 2 != 0, numbers))


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))

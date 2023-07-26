def numbers_searching(*args):
    min_number = min(args)
    max_number = max(args)
    missing_value = 0
    duplicate_number = []

    for x in range(min_number, max_number + 1):
        if args.count(x) == 0:
            missing_value = x
        elif args.count(x) > 1:
            duplicate_number.append(x)

    return [missing_value, duplicate_number]




print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))

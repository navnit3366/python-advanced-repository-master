def func_executor(*args):
    res = []
    for el in args:
        function = el[0]
        numbers = el[1]
        res.append(function(*numbers))
    return res


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))

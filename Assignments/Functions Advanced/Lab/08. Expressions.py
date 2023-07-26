def expressions(numbers, current_result, expression=''):
    if not numbers:
        return [(expression, current_result)]
    result_plus = expressions(
        numbers[1:],
        current_result + numbers[0],
        f'{expression}+{numbers[0]}')
    result_minus = expressions(
        numbers[1:],
        current_result - numbers[0],
        f'{expression}-{numbers[0]}')
    return result_plus + result_minus


nums = list(map(int, input().split(", ")))
n = len(nums)
result = expressions(nums, 0)
[print(f'{exp}={res}') for (exp, res) in result]


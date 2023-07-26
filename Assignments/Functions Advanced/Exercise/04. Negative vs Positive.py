def neg_pos_nums(*args):
    args = args[0]
    absolute_negative_number = sum(list(filter(lambda x: x < 0, args)))
    absolute_positive_number = sum(list(filter(lambda x: x > 0, args)))

    if abs(absolute_negative_number) > absolute_positive_number:
        return f'''{absolute_negative_number}
{absolute_positive_number}
The negatives are stronger than the positives'''

    return f'''{absolute_negative_number}
{absolute_positive_number}
The positives are stronger than the negatives'''


print(neg_pos_nums(list(map(int, input().split()))))

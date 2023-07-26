def get_good_kids():
    global matrix
    res = 0
    for x in matrix:
        if 'V' in x:
            res += x.count('V')
    return res


def get_start_position():
    global matrix, n
    for x in range(n):
        if 'S' in matrix[x]:
            return [x, matrix[x].index('S')]


def santa_got_a_cookie():
    global matrix, row, col, count_of_presents, good_kids_counter
    for r in range(-1, 2):
        for c in range(-1, 2):
            if 0 <= (next_row + r) < n and 0 <= (next_col + c) < n:
                if matrix[next_row + r][next_col + c] != '-':
                    count_of_presents -= 1
                    if matrix[next_row + r][next_col + c] == 'V':
                        good_kids_counter -= 1

                matrix[next_row + r][next_col + c] = '-'


count_of_presents = int(input())
n = int(input())

matrix = [input().split() for x in range(n)]

santa_position = get_start_position()
good_kids_counter = get_good_kids()

good_kids_counter_copy = good_kids_counter

moves = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

while count_of_presents > 0 and good_kids_counter > 0:
    data = input()
    if data == 'Christmas morning':
        break

    row, col = santa_position
    next_row, next_col = row + moves[data][0], col + moves[data][1]

    if 0 <= next_row < n and 0 <= next_col < n:
        matrix[row][col] = '-'
        matrix_position = matrix[next_row][next_col]

        santa_position = [next_row, next_col]

        if matrix_position == 'V':
            count_of_presents -= 1
            good_kids_counter -= 1

        elif matrix_position == 'C':
            santa_got_a_cookie()

        matrix[next_row][next_col] = 'S'

if count_of_presents == 0 and good_kids_counter > 0:
    print('Santa ran out of presents!')

[print(' '.join(x)) for x in matrix]
if good_kids_counter == 0:
    print(f'Good job, Santa! {good_kids_counter_copy} happy nice kid/s.')
else:
    print(f'No presents for {good_kids_counter} nice kid/s.')
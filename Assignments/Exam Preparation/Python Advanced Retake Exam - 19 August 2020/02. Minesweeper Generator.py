def is_valid(x, y, field):
    global n
    res = [[0, 0], [0, 0]]

    if 0 <= x - 1:
        res[0][0] = -1
    if x + 1 < n:
        res[0][1] = +1
    if 0 <= y - 1:
        res[1][0] = -1
    if y + 1 < n:
        res[1][1] = +1

    return res


n = int(input())
matrix = [[0 for y in range(n)] for x in range(n)]
bomb_number = int(input())

for i in range(bomb_number):
    pos = eval(input())
    r = pos[0]
    c = pos[1]

    matrix[r][c] = '*'

for cell in range(n):
    for position in range(n):
        number = matrix[cell][position]
        bombs_near = 0

        if number != '*':
            [row_start, row_end], [col_start, col_end] = is_valid(cell, position, matrix)

            for row in range(row_start, row_end + 1):
                for col in range(col_start, col_end + 1):
                    if matrix[cell + row][position + col] == '*':
                        bombs_near += 1
            matrix[cell][position] = bombs_near

[print(' '.join([str(y) for y in x])) for x in matrix]

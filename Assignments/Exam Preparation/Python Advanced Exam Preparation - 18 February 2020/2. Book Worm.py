word = input()
n = int(input())
worm_position = ()
matrix = []

for i in range(n):
    line = [x for x in input()]
    matrix.append(line)

    if 'P' in line:
        worm_position = (i, line.index('P'))

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
         }

number_of_moves = int(input())

for i in range(number_of_moves):
    move = input()
    cur_row, cur_col = worm_position
    nxt_row, nxt_col = moves[move]

    if 0 <= (cur_row + nxt_row) < n and 0 <= (cur_col + nxt_col) < n:
        letter = matrix[cur_row + nxt_row][cur_col + nxt_col]
        if letter.isalpha() and letter != 'P':
            word += letter

        matrix[cur_row][cur_col] = '-'

        cur_row += nxt_row
        cur_col += nxt_col

        worm_position = (cur_row, cur_col)
        matrix[cur_row][cur_col] = 'P'

    else:
        word = word[:-1]


print(word)
[print(''.join(x)) for x in matrix]
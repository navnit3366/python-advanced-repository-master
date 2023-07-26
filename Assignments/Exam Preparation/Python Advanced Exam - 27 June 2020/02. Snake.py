def get_snake_position():
    global matrix
    for r in range(n):
        if 'S' in matrix[r]:
            for c in range(n):
                if matrix[r][c] == 'S':
                    return [r, c]
                    # get the index with the .index() method


def get_burrows_indexes(field):
    global n
    res = []
    for x in range(n):
        if 'B' in field[x]:
            res.append([x, field[x].index('B')])
    return res


def is_valid(row1, col1, row2, col2):
    global n
    return 0 <= (row1 + row2) < n and 0 <= (col1 + col2) < n


moves = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1]
}

n = int(input())
matrix = [[x for x in input()[:n]] for _ in range(n)]
burrows = get_burrows_indexes(field=matrix)
food_quantity = 0

while True:
    current_row, current_col = get_snake_position()
    current_move = input()
    next_row, next_col = moves[current_move]

    if not is_valid(current_row, current_col, next_row, next_col):
        matrix[current_row][current_col] = '.'
        print('Game over!')
        break

    matrix[current_row][current_col] = '.'
    next_snake_position = matrix[current_row + next_row][current_col + next_col]

    if next_snake_position == '*':
        current_row, current_col = current_row + next_row, current_col + next_col
        food_quantity += 1
        if food_quantity == 10:
            print('You won! You fed the snake.')
            matrix[current_row][current_col] = 'S'
            break

    elif next_snake_position == 'B':
        for burrow in burrows:
            if [current_row + next_row, current_col + next_col] != burrow:
                matrix[current_row + next_row][current_col + next_col] = '.'
                current_row, current_col = burrow

    else:
        current_row, current_col = current_row + next_row, current_col + next_col

    matrix[current_row][current_col] = 'S'

print(f'Food eaten: {food_quantity}')
[print(''.join(x)) for x in matrix]

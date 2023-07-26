rows, columns = list(map(int, input().split()))
matrix = []
matrix_cells = []
equal_cells_counter = 0

for _ in range(rows):
    matrix.append(list(input().split())[:columns])

for row in range(0, rows -1):
    for col in range(0, columns - 1):
        matrix_cells.append([matrix[row][col], matrix[row][col + 1], matrix[row + 1][col], matrix[row + 1][col + 1]])

for cell in matrix_cells:
    is_equal = False

    if cell.count(cell[0]) == 4:
        if matrix_cells.count(cell) > 1:
            equal_cells_counter += 1
        elif matrix_cells.count(cell) == 1:
            equal_cells_counter += 1

print(equal_cells_counter)
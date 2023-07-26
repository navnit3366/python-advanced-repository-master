n, m = list(map(int, input().split()))
rectangular_matrix = []
biggest_square = [-100000, [], [], []]

for _ in range(n):
    rectangular_matrix.append(list(map(int, input().split()[:m])))

for row in range(0, n - 2):
    for col in range(0, m - 2):
        first_row = [rectangular_matrix[row][col], rectangular_matrix[row][col + 1], rectangular_matrix[row][col + 2]]
        second_row = [rectangular_matrix[row + 1][col], rectangular_matrix[row + 1][col + 1],
                      rectangular_matrix[row + 1][col + 2]]
        third_row = [rectangular_matrix[row + 2][col], rectangular_matrix[row + 2][col + 1],
                     rectangular_matrix[row + 2][col + 2]]
        rows_sum = sum(first_row) + sum(second_row) + sum(third_row)

        if rows_sum > biggest_square[0]:
            biggest_square[0] = rows_sum
            biggest_square[1] = first_row
            biggest_square[2] = second_row
            biggest_square[3] = third_row

print(f"Sum = {biggest_square[0]}")
[print(x, end=" ") for x in biggest_square[1]]
print()
[print(x, end=" ") for x in biggest_square[2]]
print()
[print(x, end=" ") for x in biggest_square[3]]

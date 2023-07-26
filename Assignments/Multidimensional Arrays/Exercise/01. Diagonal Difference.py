n = int(input())
matrix = []
first_diagonal = 0
second_diagonal = 0

for _ in range(n):
    matrix.append(list(map(int, input().split())))

for i in range(n):
    first_diagonal += matrix[i][n - 1 - i]

for i in range(n - 1, -1, -1):
    second_diagonal += matrix[i][i]

print(abs(first_diagonal - second_diagonal))

def is_valid(r: int, c: int):
    global n

    return (-1 < r < n) and (-1 < c < n)


n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

tokens = input()
while tokens != "END":
    tokens = tokens.split()
    cmd = tokens[0]
    row = int(tokens[1])
    col = int(tokens[2])
    val = int(tokens[3])

    if is_valid(row, col):
        if cmd == "Add":
            matrix[row][col] += val
        else:
            matrix[row][col] -= val

    else:
        print("Invalid coordinates")

    tokens = input()

[print(" ".join([str(x) for x in i])) for i in matrix]

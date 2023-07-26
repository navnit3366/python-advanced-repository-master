rows, columns = list(map(int, input().split()))
matrix = []

for _ in range(rows):
    matrix.append(list(input().split())[:columns])

while True:
    cmd = input().split()

    if cmd[0] == "END" and len(cmd) == 1:
        break

    if len(cmd) == 5:
        cond = (0 <= int(cmd[1]) < rows) and (0 <= int(cmd[2]) < columns) and (0 <= int(cmd[3]) < rows) and (0 <= int(cmd[4]) < columns)
        if cmd[0] == "swap" and cond:
            matrix[int(cmd[1])][int(cmd[2])], matrix[int(cmd[3])][int(cmd[4])] = matrix[int(cmd[3])][int(cmd[4])], matrix[int(cmd[1])][int(cmd[2])]
            for i in range(rows):
                print(" ".join(matrix[i]))
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
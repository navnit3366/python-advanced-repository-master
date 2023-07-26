from collections import deque


def get_start_position(count: int):
    for x_ind in range(count):
        if "s" in matrix[x_ind]:
            for y_ind in range(count):
                if matrix[x_ind][y_ind] == "s":
                    return [x_ind, y_ind]


def make_a_move(move: str):
    global game_over, coals_collected, current_position, row, col

    if move == "up":
        if row - 1 >= 0:
            current_position = [row - 1, col]

    elif move == "down":
        if row + 1 < len(matrix):
            current_position = [row + 1, col]

    elif move == "left":
        if col - 1 >= 0:
            current_position = [row, col - 1]

    elif move == "right":
        if col + 1 < len(matrix):
            current_position = [row, col + 1]

    if matrix[current_position[0]][current_position[1]] == "e":
        game_over = True
    elif matrix[current_position[0]][current_position[1]] == "c":
        coals_collected += 1
    matrix[current_position[0]][current_position[1]] = "*"


n = int(input())
move_commands = deque(input().split())
matrix = deque([x for x in input().split()] for i in range(n))
current_position = get_start_position(n)

game_over = False
all_coals = sum(list(map(lambda x: x.count("c"), matrix)))
coals_collected = 0

while True:
    current_move = move_commands.popleft()
    row = current_position[0]
    col = current_position[1]

    make_a_move(current_move)

    if game_over:
        print(f"Game over! ({current_position[0]}, {current_position[1]})")
        break
    elif coals_collected == all_coals:
        print(f"You collected all coals! ({current_position[0]}, {current_position[1]})")
        break
    elif not move_commands:
        print(f"{all_coals - coals_collected} coals left. ({current_position[0]}, {current_position[1]})")
        break

with open('text.txt', 'r') as file:
    for line_ind, line in enumerate(file):
        if line_ind % 2 == 0:
            for symbol in "-,.!?":
                line = line.replace(symbol, "@")

            print(" ".join(reversed(line.split())))

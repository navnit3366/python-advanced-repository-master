text = input()
stack = []

for i in range(len(text)):
    if text[i] == "(":
        stack.append(i)

    elif text[i] == ")":
        print(text[stack.pop(): i + 1])

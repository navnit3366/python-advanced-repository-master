def balanced(text: str):
    stack = []
    is_balanced = True

    for i in range(len(text)):
        if text[i] in "{[(":
            stack.append(i)

        elif text[i] in ")]}" and len(stack) > 0:
            start_ind = stack.pop()

            if text[start_ind] == "{":
                if text[i] != "}":
                    is_balanced = False
                    break
            elif text[start_ind] == "[":
                if text[i] != "]":
                    is_balanced = False
                    break
            elif text[start_ind] == "(":
                if text[i] != ")":
                    is_balanced = False
                    break
            else:
                is_balanced = False
                break

        else:
            is_balanced = False
            break

    if is_balanced and len(text) > 0 and len(stack) == 0:
        print("YES")
    else:
        print("NO")


balanced(text=input())

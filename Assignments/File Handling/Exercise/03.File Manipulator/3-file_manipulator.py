import os

tokens = input()
while tokens != "End":
    tokens = tokens.split("-")
    cmd = tokens[0]
    file_name = tokens[1]

    if cmd == 'Create':
        with open(file_name, 'w') as file:
            file.write("")

    elif cmd == 'Add':
        content = tokens[2]

        with open(file_name, 'a') as file:
            file.write(f'{content}\n')

    elif cmd == 'Replace':
        old_string = tokens[2]
        new_string = tokens[3]

        if os.path.exists(file_name):
            with open(file_name, 'r') as file:
                file_text = file.read()

            file_text = file_text.replace(old_string, new_string)

            with open(file_name, 'w') as file:
                file.write(file_text)

        else:
            print('An error occurred')

    elif cmd == 'Delete':
        if os.path.exists(file_name):
            os.remove(file_name)
        else:
            print('An error occurred')

    tokens = input()

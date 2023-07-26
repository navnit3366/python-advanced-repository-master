text = ''
with open('text.txt', 'r') as file:
    for (line_ind, line) in enumerate(file):
        letters_count = len([x for x in line if x.isalpha()])
        punctuation_count = len([x for x in line if x in '.,:;!?-_\'"'])
        # for letter in line:
        #     if letter.isalpha():
        #         letters_count += 1
        #     elif letter in '.,:;!?-_\'"':
        #         punctuation_count += 1

        text += f"Line {line_ind + 1}: {line[:-2]} ({letters_count})({punctuation_count})\n"

with open('output.txt', 'w') as  file:
    file.write(text)

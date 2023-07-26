import os

path = input()
path_sep_count = path.count(os.path.sep)
files_extension_dict = {}

for root, dirs, files in os.walk(path):
    if (path_sep_count - root.count(os.path.sep)) <= 1:
        for file in files:
            extension = file.split('.')[-1]
            if extension not in files_extension_dict:
                files_extension_dict[extension] = []
            files_extension_dict[extension].append(file)

text = ''
for ext, files in sorted(files_extension_dict.items()):
    text += f'.{ext}\n'
    for file in sorted(files):
        text += f'- - - {file}\n'

desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
final_path = desktop_path + os.path.sep + 'report.txt'

with open(final_path, 'w') as file:
    file.write(text)

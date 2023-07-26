import os

file_path = "Resources\File Writer\my_first_file.txt"
if os.path.exists(file_path):
    os.remove(file_path)
else:
    print('File already deleted!')

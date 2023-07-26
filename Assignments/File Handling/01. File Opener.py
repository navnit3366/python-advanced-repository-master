try:
    file = open("Resources/File Opener/text.txt")
    print("File found")
except FileNotFoundError:
    print("File not found")

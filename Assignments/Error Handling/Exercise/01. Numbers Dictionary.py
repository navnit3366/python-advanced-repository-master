numbers_dictionary = {}
try:
    line = input()
    while line != 'Search':
        txt_number = int(input())
        numbers_dictionary[line] = txt_number
        line = input()

    while True:
        line = input()
        if line == 'Remove':
            break
        print(numbers_dictionary[line])

    while True:
        line = input()
        if line == 'End':
            break
        del numbers_dictionary[line]

except ValueError:
    print('The variable number must be an integer')

except (NameError, KeyError):
    print('Number does not exist in dictionary')

print(numbers_dictionary)

from my_package import fibonacci

seq = []
while True:
    data = input()

    if data == "Stop":
        break

    data = data.split()
    cmd = data[0]

    if cmd == "Create" and data[1] == "Sequence":
        number = int(data[2])
        seq = fibonacci.create(number)
        print(" ".join([str(x) for x in seq]))

    elif cmd == "Locate":
        number = int(data[1])
        number_index = fibonacci.locate(number, seq)
        if len(number_index) > 0:
            print(f"The number - {number} is at index {number_index[0]}")
        else:
            print(f"The number {number} is not in the sequence")

# print(' '.join([str(x) for x in fibonacci.create(int(input()))])


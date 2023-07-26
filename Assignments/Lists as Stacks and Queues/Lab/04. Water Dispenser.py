from collections import deque

water_in_dispenser = int(input())
people = deque()
while True:
    cmd = input()

    if cmd == "Start":
        break
    else:
        people.append(cmd)

while True:
    cmd = input()

    if cmd == "End":
        print(f"{water_in_dispenser} liters left")
        break
    elif cmd.startswith("refill "):
        water_in_dispenser += int(cmd[7:])
    else:
        person = people.popleft()
        if int(cmd) > water_in_dispenser:
            print(f"{person} must wait")

        else:
            water_in_dispenser -= int(cmd)
            print(f"{person} got water")

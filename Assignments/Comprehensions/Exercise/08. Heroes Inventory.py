heroes_items = {k: {} for k in input().split(", ")}

cmd = input()
while cmd != "End":
    cmd = cmd.split("-")

    name = cmd[0]
    item = cmd[1]
    item_cost = int(cmd[2])

    if item not in heroes_items[name]:
        heroes_items[name][item] = item_cost
    cmd = input()

[print(f"{x} -> Items: {len(heroes_items[x])}, Cost: {sum(heroes_items[x].values())}") for x in heroes_items.keys()]

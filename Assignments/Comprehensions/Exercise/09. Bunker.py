items = {key: {} for key in input().split(", ")}
n = int(input())

for _ in range(n):
    line = input().split(" - ")
    category, item = line[0], line[1]
    items_count = line[2].split(";")
    quantity = int(items_count[0].split(":")[1])
    quality = int(items_count[1].split(":")[1])

    items[category][item] = (quantity, quality)

items_count = sum([sum([i[0] for i in list(items[x].values())]) for x in items])
avg_quality = sum([sum([i[1] for i in list(items[x].values())]) for x in items]) / len([x for x in items.keys()])

print(f"Count of items: {items_count}")
print(f"Average quality: {avg_quality:.2f}")
[print(f"{x} -> {', '.join(items[x])}") for x in items.keys()]

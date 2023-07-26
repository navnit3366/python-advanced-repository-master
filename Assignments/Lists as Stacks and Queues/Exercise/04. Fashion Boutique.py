clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
rack_sum = 0
racks_count = 0

while clothes:
    current = clothes.pop()

    if (rack_sum + current) > rack_capacity:
        racks_count += 1
        rack_sum = 0
        clothes.append(current)

    elif (rack_sum + current) == rack_capacity:
        racks_count += 1
        rack_sum = 0

    else:
        rack_sum += current

if rack_sum > 0 :
    racks_count += 1

print(racks_count)

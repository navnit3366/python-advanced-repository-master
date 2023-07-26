elements = {x: len(x) for x in input().split(", ")}
res= [f"{key} -> {value}" for key, value in elements.items()]
print(", ".join(res))

# line = input().split(", ")
# res = [f"{x} -> {len(x)}" for x in line]
# print(", ".join(res))


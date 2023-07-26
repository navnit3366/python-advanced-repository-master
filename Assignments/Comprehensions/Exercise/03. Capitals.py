countries = input().split(", ")
capitals = input().split(", ")
res = {key: value for (key, value) in zip(countries, capitals)}
[print(f"{x} -> {y}") for x, y in res.items()]

elements = [[i for i in x.split()] for x in input().split("|")]
elements_reversed = [x for x in reversed(elements)]
[[print(i, end=" ") for i in x] for x in elements_reversed]

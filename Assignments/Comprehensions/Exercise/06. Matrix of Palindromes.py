row, col = [int(x) for x in input().split()]
matrix = [[f"{chr(r)}{chr(r + c)}{chr(r)}" for c in range(col)] for r in range(97, 97 + row)]
[print(" ".join(x)) for x in matrix]

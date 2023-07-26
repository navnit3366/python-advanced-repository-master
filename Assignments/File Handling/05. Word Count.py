import re

with open('Resources\Words Count\words.txt') as f:
    words = f.readline().split()

with open('Resources\Words Count\input.txt') as f:
    text = f.read()

matches = {}
for word in words:
    match = re.findall(rf'[\s-]({word})[\s.,?!]', text, re.MULTILINE + re.IGNORECASE)
    matches[word] = len(match)

matches_sorted = sorted(matches.items(), key=lambda x: x[1], reverse=True)
[print(f"{k} - {v}") for (k, v) in matches_sorted]

from collections import deque

words = deque(input().split())
colors = {"red", "yellow", "blue", "orange", "purple", "green"}
req_colors = {
    "orange": { "red", "yellow" },
    "purple": { "red", "blue" },
    "green": { "yellow", "blue" }
}

crafted_colors = []

while words:
    first = words.popleft()
    last = words.pop() if words else ""

    for color in (first + last, last + first):
        if color in colors:
            crafted_colors.append(color)
            break
    else:
        for el in (first[:-1], last[:-1]):
            if el:
                words.insert(len(words) // 2, el)

for color in set(req_colors.keys()).intersection(crafted_colors):
    if not req_colors[color].issubset(crafted_colors):
        crafted_colors.remove(color)

print(crafted_colors)
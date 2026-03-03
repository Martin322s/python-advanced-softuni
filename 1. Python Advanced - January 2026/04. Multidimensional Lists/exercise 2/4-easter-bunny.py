n = int(input())
field = []
bunny_r = 0
bunny_c = 0

for r in range(n):
    row = input().split()
    field.append(row)
    for c in range(n):
        if row[c] == "B":
            bunny_r, bunny_c = r, c

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

best_dir = ""
best_sum = -10**18
best_path = []

for name, (dr, dc) in directions.items():
    r = bunny_r + dr
    c = bunny_c + dc
    current_sum = 0
    path = []

    while 0 <= r < n and 0 <= c < n:
        if field[r][c] == "X":
            break

        current_sum += int(field[r][c])
        path.append([r, c])

        r += dr
        c += dc

    if path and current_sum > best_sum:
        best_sum = current_sum
        best_dir = name
        best_path = path

print(best_dir)
for pos in best_path:
    print(pos)
print(best_sum)
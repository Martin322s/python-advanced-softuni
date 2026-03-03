n = int(input())
field = []
alice_r = 0
alice_c = 0

for r in range(n):
    row = input().split()
    field.append(row)
    for c in range(n):
        if row[c] == "A":
            alice_r, alice_c = r, c

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

tea = 0
field[alice_r][alice_c] = "*"

while tea < 10:
    command = input()
    dr, dc = moves[command]

    new_r = alice_r + dr
    new_c = alice_c + dc

    if not (0 <= new_r < n and 0 <= new_c < n):
        print("Alice didn't make it to the tea party.")
        break

    cell = field[new_r][new_c]

    if cell == "R":
        field[new_r][new_c] = "*"
        print("Alice didn't make it to the tea party.")
        break

    if cell.isdigit():
        tea += int(cell)

    field[new_r][new_c] = "*"
    alice_r, alice_c = new_r, new_c

else:
    print("She did it! She went to the party.")

for row in field:
    print(" ".join(row))
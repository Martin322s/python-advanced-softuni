rows, cols = map(int, input().split())

lair = []
player_row = player_col = 0

for r in range(rows):
    line = list(input().strip())
    lair.append(line)
    if "P" in line:
        player_row = r
        player_col = line.index("P")

commands = input().strip()

moves = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0),
}

won = False
dead = False
last_row, last_col = player_row, player_col

for cmd in commands:
    dr, dc = moves[cmd]

    lair[player_row][player_col] = "."

    new_row = player_row + dr
    new_col = player_col + dc

    if not (0 <= new_row < rows and 0 <= new_col < cols):
        won = True
        last_row, last_col = player_row, player_col
    else:
        if lair[new_row][new_col] == "B":
            dead = True
            last_row, last_col = new_row, new_col
        else:
            player_row, player_col = new_row, new_col
            lair[player_row][player_col] = "P"
            last_row, last_col = player_row, player_col

    bunnies = []
    for r in range(rows):
        for c in range(cols):
            if lair[r][c] == "B":
                bunnies.append((r, c))

    for r, c in bunnies:
        for br, bc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + br, c + bc
            if 0 <= nr < rows and 0 <= nc < cols:
                if lair[nr][nc] == "P":
                    dead = True
                    last_row, last_col = nr, nc
                lair[nr][nc] = "B"

    if won or dead:
        break

for r in lair:
    print("".join(r))

if won:
    print(f"won: {last_row} {last_col}")
else:
    print(f"dead: {last_row} {last_col}")
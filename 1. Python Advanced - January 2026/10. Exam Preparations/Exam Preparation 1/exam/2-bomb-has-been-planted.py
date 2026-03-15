def in_bounds(r, c, rows, cols):
    return 0 <= r < rows and 0 <= c < cols

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

rows, cols = [int(x) for x in input().split(", ")]

matrix = []
start_pos = None
bomb_pos = None

for r in range(rows):
    row = list(input())

    if "C" in row:
        start_pos = (r, row.index("C"))

    if "B" in row:
        bomb_pos = (r, row.index("B"))

    matrix.append(row)

cur_r, cur_c = start_pos
seconds = 16

finished = False
output = []

while seconds > 0 and not finished:
    cmd = input()

    if cmd == "defuse":
        if (cur_r, cur_c) != bomb_pos:
            seconds -= 2
            continue

        seconds -= 4
        br, bc = bomb_pos

        if seconds >= 0:
            matrix[br][bc] = "D"
            output.append("Counter-terrorist wins!")
            output.append(f"Bomb has been defused: {seconds} second/s remaining.")
        else:
            matrix[br][bc] = "X"
            output.append("Terrorists win!")
            output.append("Bomb was not defused successfully!")
            output.append(f"Time needed: {abs(seconds)} second/s.")
        finished = True
        break

    seconds -= 1
    dr, dc = moves[cmd]
    nr, nc = cur_r + dr, cur_c + dc

    if not in_bounds(nr, nc, rows, cols):
        continue

    cur_r, cur_c = nr, nc

    if matrix[cur_r][cur_c] == "T":
        matrix[cur_r][cur_c] = "*"
        output.append("Terrorists win!")
        finished = True
        break

if not finished and seconds <= 0:
    output.append("Terrorists win!")
    output.append("Bomb was not defused successfully!")
    output.append("Time needed: 0 second/s.")

sr, sc = start_pos
matrix[sr][sc] = "C"

print("\n".join(output))
for row in matrix:
    print("".join(row))
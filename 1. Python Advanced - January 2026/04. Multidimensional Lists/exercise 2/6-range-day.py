SIZE = 5

field = []
a_r = a_c = 0
total_targets = 0

for r in range(SIZE):
    row = input().split()
    field.append(row)
    for c in range(SIZE):
        if row[c] == "A":
            a_r, a_c = r, c
        elif row[c] == "x":
            total_targets += 1

commands_count = int(input())

dirs = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

hit_positions = []
hit_count = 0

def in_bounds(r, c):
    return 0 <= r < SIZE and 0 <= c < SIZE

for _ in range(commands_count):
    parts = input().split()
    action = parts[0]
    direction = parts[1]
    dr, dc = dirs[direction]

    if action == "move":
        steps = int(parts[2])
        new_r = a_r + dr * steps
        new_c = a_c + dc * steps

        if in_bounds(new_r, new_c) and field[new_r][new_c] == ".":
            field[a_r][a_c] = "."
            a_r, a_c = new_r, new_c
            field[a_r][a_c] = "A"

    elif action == "shoot":
        r = a_r + dr
        c = a_c + dc

        while in_bounds(r, c):
            if field[r][c] == "x":
                field[r][c] = "."
                hit_positions.append([r, c])
                hit_count += 1
                break
            r += dr
            c += dc

    if hit_count == total_targets:
        break

left_targets = total_targets - hit_count

if left_targets == 0:
    print(f"Training completed! All {total_targets} targets hit.")
else:
    print(f"Training not completed! {left_targets} targets left.")

for pos in hit_positions:
    print(pos)
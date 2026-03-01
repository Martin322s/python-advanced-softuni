presents = int(input())
n = int(input())

neighborhood = []
santa_r = santa_c = 0
nice_kids_total = 0
nice_kids_given = 0

for r in range(n):
    row = input().split()
    neighborhood.append(row)
    for c in range(n):
        if row[c] == "S":
            santa_r, santa_c = r, c
        elif row[c] == "V":
            nice_kids_total += 1

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

def in_bounds(r, c):
    return 0 <= r < n and 0 <= c < n

def give_present_at(r, c):
    """Gives a present if there is a kid at (r,c): V or X.
       Updates counters only for nice kids (V)."""
    global presents, nice_kids_given
    if presents <= 0:
        return
    if neighborhood[r][c] == "V":
        presents -= 1
        nice_kids_given += 1
        neighborhood[r][c] = "-"
    elif neighborhood[r][c] == "X":
        presents -= 1
        neighborhood[r][c] = "-"

while True:
    command = input()
    if command == "Christmas morning":
        break

    dr, dc = moves[command]
    new_r = santa_r + dr
    new_c = santa_c + dc

    neighborhood[santa_r][santa_c] = "-"

    santa_r, santa_c = new_r, new_c

    cell = neighborhood[santa_r][santa_c]

    if cell == "V":
        presents -= 1
        nice_kids_given += 1
        neighborhood[santa_r][santa_c] = "-"
    elif cell == "C":
        neighborhood[santa_r][santa_c] = "-"

        for r_add, c_add in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            rr = santa_r + r_add
            cc = santa_c + c_add
            if in_bounds(rr, cc) and neighborhood[rr][cc] in ("V", "X"):
                give_present_at(rr, cc)
                if presents == 0:
                    break
 
    neighborhood[santa_r][santa_c] = "S"

    if presents == 0:
        break

if presents == 0 and nice_kids_given < nice_kids_total:
    print("Santa ran out of presents!")

for row in neighborhood:
    print(" ".join(row))

left_nice = nice_kids_total - nice_kids_given
if left_nice == 0:
    print(f"Good job, Santa! {nice_kids_given} happy nice kid/s.")
else:
    print(f"No presents for {left_nice} nice kid/s.")

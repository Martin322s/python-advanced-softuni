rows, cols = map(int, input().split())
matrix = [list(input()) for _ in range(rows)]

start_row = start_col = 0
for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == "B":
            start_row, start_col = r, c

current_row, current_col = start_row, start_col
matrix[start_row][start_col] = "-"

has_pizza = False
delivery_canceled = False

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    command = input()
    delta_row, delta_col = directions[command]

    next_row = current_row + delta_row
    next_col = current_col + delta_col

    if not (0 <= next_row < rows and 0 <= next_col < cols):
        print("The delivery is late. Order is canceled.")
        delivery_canceled = True
        break

    if matrix[next_row][next_col] == "*":
        continue

    current_row, current_col = next_row, next_col
    current_cell = matrix[current_row][current_col]

    if current_cell == "-":
        matrix[current_row][current_col] = "."

    if current_cell == "P" and not has_pizza:
        has_pizza = True
        matrix[current_row][current_col] = "R"
        print("Pizza is collected. 10 minutes for delivery.")
        continue

    if current_cell == "A" and has_pizza:
        matrix[current_row][current_col] = "P"
        print("Pizza is delivered on time! Next order...")
        break

if delivery_canceled:
    matrix[start_row][start_col] = " "
else:
    matrix[start_row][start_col] = "B"

for row in matrix:
    print("".join(row))
n = int(input())

matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split()])

bombs_input = input().split()

directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]

for bomb in bombs_input:
    row_str, col_str = bomb.split(",")
    row = int(row_str)
    col = int(col_str)

    if matrix[row][col] <= 0:
        continue

    bomb_power = matrix[row][col]

    for dr, dc in directions:
        r = row + dr
        c = col + dc

        if 0 <= r < n and 0 <= c < n:
            if matrix[r][c] > 0:
                matrix[r][c] -= bomb_power

    matrix[row][col] = 0

alive_cells = 0
alive_sum = 0

for r in range(n):
    for c in range(n):
        if matrix[r][c] > 0:
            alive_cells += 1
            alive_sum += matrix[r][c]

print(f"Alive cells: {alive_cells}")
print(f"Sum: {alive_sum}")

for row in matrix:
    print(" ".join(str(x) for x in row))
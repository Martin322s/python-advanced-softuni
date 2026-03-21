grid_size = int(input())
grid = [list(input()) for _ in range(grid_size)]

pacman_row = pacman_col = 0
total_stars = 0

for row in range(grid_size):
    for col in range(grid_size):
        if grid[row][col] == 'P':
            pacman_row, pacman_col = row, col
        if grid[row][col] == '*':
            total_stars += 1

health = 100
remaining_stars = total_stars
has_immunity = False
first_move = True

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:
    command = input()

    if command == "end":
        break

    if first_move:
        grid[pacman_row][pacman_col] = '-'
        first_move = False

    delta_row, delta_col = directions[command]
    next_row = (pacman_row + delta_row) % grid_size
    next_col = (pacman_col + delta_col) % grid_size

    cell = grid[next_row][next_col]

    if cell == '*':
        remaining_stars -= 1
        grid[next_row][next_col] = '-'

    elif cell == 'G':
        if not has_immunity:
            health -= 50
        else:
            has_immunity = False
        grid[next_row][next_col] = '-'

    elif cell == 'F':
        has_immunity = True
        grid[next_row][next_col] = '-'

    pacman_row, pacman_col = next_row, next_col

    if health == 0 or remaining_stars == 0:
        break

grid[pacman_row][pacman_col] = 'P'

if health == 0:
    print(f"Game over! Pacman last coordinates [{pacman_row},{pacman_col}]")
elif remaining_stars == 0:
    print("Pacman wins! All the stars are collected.")
else:
    print("Pacman failed to collect all the stars.")

print(f"Health: {health}")

if remaining_stars > 0:
    print(f"Uncollected stars: {remaining_stars}")

for row in grid:
    print("".join(row))
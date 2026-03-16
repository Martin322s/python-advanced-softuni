n = int(input())

matrix = []
ship_row = ship_col = 0

for r in range(n):
    row = input().split()
    matrix.append(row)
    if 'S' in row:
        ship_row = r
        ship_col = row.index('S')

resources = 100
matrix[ship_row][ship_col] = '.'

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

mission_success = False
lost_in_space = False

while True:
    command = input()

    dr, dc = directions[command]
    new_row = ship_row + dr
    new_col = ship_col + dc

    if not (0 <= new_row < n and 0 <= new_col < n):
        lost_in_space = True
        break

    resources -= 5
    ship_row, ship_col = new_row, new_col

    cell = matrix[ship_row][ship_col]

    if cell == 'M':
        resources -= 5
        matrix[ship_row][ship_col] = '.'

    elif cell == 'R':
        resources = min(100, resources + 10)

    elif cell == 'P':
        mission_success = True
        break

    if resources < 5:
        break

if mission_success:
    print(f"Mission accomplished! The spaceship reached Planet B with {resources} resources left.")
elif lost_in_space:
    print("Mission failed! The spaceship was lost in space.")
else:
    print("Mission failed! The spaceship was stranded in space.")

if not mission_success:
    matrix[ship_row][ship_col] = 'S'

for row in matrix:
    print(' '.join(row))
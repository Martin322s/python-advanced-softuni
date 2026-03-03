rows = int(input())
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

while True:
    command = input()

    if command == "END":
        break

    parts = command.split()
    action = parts[0]
    row = int(parts[1])
    col = int(parts[2])
    value = int(parts[3])

    if 0 <= row < rows and 0 <= col < len(matrix[0]):
        if action == "Add":
            matrix[row][col] += value
        elif action == "Subtract":
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")

for row in matrix:
    print(*row)
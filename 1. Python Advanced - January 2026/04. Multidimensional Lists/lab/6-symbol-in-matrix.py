matrix_size = int(input())

matrix = []

for _ in range(matrix_size):
    content = input()
    row = []

    for i in range(len(content)):
        row.append(content[i])

    matrix.append(row)

x_idx = 0
y_idx = 0
is_found = False

searched_symbol = input()

for i in range(matrix_size):
    for j in range(matrix_size):
        current_symbol = matrix[i][j]

        if current_symbol == searched_symbol:
            x_idx = i
            y_idx = j
            is_found = True
            break
    if is_found: break

if is_found:
    print(f"({x_idx}, {y_idx})")
else:
    print(f"{searched_symbol} does not occur in the matrix")
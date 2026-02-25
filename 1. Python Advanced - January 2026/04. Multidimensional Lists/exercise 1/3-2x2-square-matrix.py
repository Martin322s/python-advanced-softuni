rows, cols = [int(x) for x in input().split(" ")]
matrix = []

for _ in range(rows):
    matrix.append([x for x in input().split(" ")])

equal_block = 0

for row in range(rows - 1):
    for col in range(cols - 1):
        symbol = matrix[row][col]

        if symbol == matrix[row + 1][col] and symbol == matrix[row + 1][col + 1] and symbol == matrix[row][col + 1]:
            equal_block += 1

print(equal_block)
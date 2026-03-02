rows, cols = [int(x) for x in input().split(", ")]

matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

best_sum = float("-inf")
best_submatrix = []

for r in range(rows - 1):
    for c in range(cols - 1):
        a = matrix[r][c]
        b = matrix[r][c + 1]
        c2 = matrix[r + 1][c]
        d = matrix[r + 1][c + 1]

        current_sum = a + b + c2 + d

        if current_sum > best_sum:
            best_sum = current_sum
            best_submatrix = [[a, b], [c2, d]]

print(*best_submatrix[0])
print(*best_submatrix[1])
print(best_sum)
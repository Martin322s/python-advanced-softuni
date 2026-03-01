n_rows, n_cols = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(n_rows):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)

total_sum = 0
for row in matrix:
    total_sum += sum(row)

print(total_sum)
print(matrix, end="")  
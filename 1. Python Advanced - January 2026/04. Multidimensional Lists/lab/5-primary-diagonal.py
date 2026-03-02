matrix_size = int(input())
matrix = []

for _ in range(matrix_size):
    row = [int(x) for x in input().split(" ")]
    matrix.append(row)

primary_diagonal_sum = 0

for i in range(matrix_size):
    primary_diagonal_sum += matrix[i][i]

print(primary_diagonal_sum)
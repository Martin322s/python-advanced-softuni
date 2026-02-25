matrix_size = int(input())

matrix = []

for _ in range(matrix_size):
    row = [int(x) for x in input().split(" ")]
    matrix.append(row)

primary_diagonal_sum = sum([matrix[i][i] for i in range(matrix_size)])
secondary_diagonal_sum = sum([matrix[i][matrix_size - 1 - i] for i in range(matrix_size)])
difference = abs(primary_diagonal_sum - secondary_diagonal_sum)

print(difference)
rows, cols = [int(x) for x in input().split(" ")]
matrix = [[int(x) for x in input().split(" ")] for _ in range(rows)]

max_sum = float('-inf')
max_sum_matrix = []

for row in range(rows - 2):
    for col in range(cols - 2):
        current_sum = (
            matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] +
            matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2] +
            matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]
        )

        max_sum_matrix_candidate = [
            [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]],
            [matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2]],
            [matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]],
        ]

        if current_sum > max_sum:
            max_sum = current_sum
            max_sum_matrix = max_sum_matrix_candidate

print(f"Sum = {max_sum}")
print('\n'.join([' '.join([str(x) for x in row]) for row in max_sum_matrix]))
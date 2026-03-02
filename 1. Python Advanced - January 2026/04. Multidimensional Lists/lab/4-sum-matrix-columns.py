n_rows, n_cols = [int(x) for x in input().split(", ")]
matrix = []

for _ in range(n_rows):
    row = [int(x) for x in input().split(" ")]
    matrix.append(row)

for i in range(n_cols):
    col_sum = 0

    for j in range(n_rows):
        col_sum += matrix[j][i]
    
    print(col_sum)
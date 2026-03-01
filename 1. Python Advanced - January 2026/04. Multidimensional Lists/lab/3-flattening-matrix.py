n_rows = int(input())
matrix = []

for _ in range(n_rows):
    row = [x for x in input().split(", ")]
    matrix.append(row)

flattned_matrix = [int(x) for row in matrix for x in row]

print(flattned_matrix)
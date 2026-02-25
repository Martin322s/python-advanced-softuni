n = int(input())

matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]

primary = [matrix[i][i] for i in range(n)]
secondary = [matrix[i][n - 1 - i] for i in range(n)]

print(f"Primary diagonal: {', '.join(map(str, primary))}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join(map(str, secondary))}. Sum: {sum(secondary)}")
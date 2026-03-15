def print_triangle(n):
    for row in range(1, n + 1):
        print(*range(1, row + 1))

    for row in range(n - 1, 0, -1):
        print(*range(1, row + 1))
n = int(input())
board = [list(input().strip()) for _ in range(n)]

moves = [
    (-2, -1), (-2,  1),
    (-1, -2), (-1,  2),
    ( 1, -2), ( 1,  2),
    ( 2, -1), ( 2,  1)
]

def in_bounds(r, c):
    return 0 <= r < n and 0 <= c < n

def attacks_count(r, c):
    cnt = 0
    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if in_bounds(nr, nc) and board[nr][nc] == "K":
            cnt += 1
    return cnt

removed = 0

while True:
    max_attacks = 0
    best_r = -1
    best_c = -1

    for r in range(n):
        for c in range(n):
            if board[r][c] == "K":
                current = attacks_count(r, c)
                if current > max_attacks:
                    max_attacks = current
                    best_r = r
                    best_c = c

    if max_attacks == 0:
        break

    board[best_r][best_c] = "0"
    removed += 1

print(removed)
from collections import deque

rows, cols = [int(x) for x in input().split()]
word = input()

letters = deque(word)

for r in range(rows):
    row_chars = []

    for _ in range(cols):
        if not letters:
            letters = deque(word)
        row_chars.append(letters.popleft())

    if r % 2 == 1:
        row_chars.reverse()

    print("".join(row_chars))
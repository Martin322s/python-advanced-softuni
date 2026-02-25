from collections import deque

bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())

total_honey = 0

functions = {
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y
}

while bees and nectar:
    bee = bees.popleft()
    curr_nectar = nectar.pop()

    if curr_nectar < bee:
        bees.appendleft(bee)
        continue

    symbol = symbols.popleft()

    if symbol == "/" and curr_nectar == 0:
        continue

    total_honey += abs(functions[symbol](bee, curr_nectar))

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
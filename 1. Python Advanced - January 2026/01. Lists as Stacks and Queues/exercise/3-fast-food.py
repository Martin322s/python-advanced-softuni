from collections import deque

food = int(input())

orders = deque([int(x) for x in input().split()])

if orders:
    print(max(orders))

for order in orders.copy():
    if food >= order:
        orders.popleft()
        food -= order
    else:
        if orders:
            print(f"Orders left: {' '.join(map(str, orders))}")
            break
else:
    print("Orders complete")
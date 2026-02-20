from collections import deque

bullet_price = int(input())
barrel_size = int(input())

bullets = [int(x) for x in input().split()]
locks = deque(int(x) for x in input().split())

intelligence_value = int(input())

shots = 0
in_barrel = barrel_size

while bullets and locks:
    bullet = bullets.pop()
    lock = locks[0]

    shots += 1
    in_barrel -= 1

    if bullet <= lock:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")

    if in_barrel == 0 and bullets:
        print("Reloading!")
        in_barrel = barrel_size

cost = shots * bullet_price

if not locks:
    earned = intelligence_value - cost
    print(f"{len(bullets)} bullets left. Earned ${earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
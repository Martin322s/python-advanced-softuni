from collections import deque

queue = deque(input().split(" "))
rotations = int(input())

while len(queue) > 1:
    queue.rotate(-(rotations - 1))
    name = queue.popleft()
    print(f"Removed {name}")

print(f"Last is {queue[0]}")
from collections import deque
from datetime import datetime, timedelta

robots = {}

for r in input().split(";"):
    name, time_needed = r.split("-")
    robots[name] = [int(time_needed), 0]

factory_time = datetime.strptime(input(), "%H:%M:%S")

products = deque()
while True:
    product = input()
    if product == "End":
        break
    products.append(product)

while products:
    factory_time += timedelta(seconds=1)
    product = products.popleft()

    free_robot = None

    for name, data in robots.items():
        if data[1] > 0:
            data[1] -= 1
        if data[1] == 0 and free_robot is None:
            free_robot = name

    if free_robot is None:
        products.append(product)
        continue

    robots[free_robot][1] = robots[free_robot][0]
    print(f"{free_robot} - {product} [{factory_time.strftime('%H:%M:%S')}]")
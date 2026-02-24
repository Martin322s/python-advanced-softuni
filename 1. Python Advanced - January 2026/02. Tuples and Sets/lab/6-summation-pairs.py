nums = list(map(int, input().split()))
target = int(input())

seen = set()

for x in nums:
    y = target - x
    if y in seen:
        print(f"{y} + {x} = {target}")
    seen.add(x)
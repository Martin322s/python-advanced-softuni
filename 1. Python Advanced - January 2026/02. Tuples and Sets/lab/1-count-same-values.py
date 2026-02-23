nums = tuple([float(x) for x in input().split()])

data = {}

for num in nums:
    if num not in data:
        data[num] = 0
    data[num] += 1

for num, count in data.items():
    print(f"{num} - {count} times")
n, m = [int(x) for x in input().split()]

first_set = set()

for _ in range(n):
    element = input()
    first_set.add(element)

second_set = set()

for _ in range(m):
    element = input()
    second_set.add(element)

common_elements = first_set.intersection(second_set)

print("\n".join(common_elements))
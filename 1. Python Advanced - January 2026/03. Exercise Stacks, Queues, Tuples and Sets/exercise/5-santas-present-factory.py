from collections import deque

materials = [int(x) for x in input().split()]
magic_levels = deque(int(x) for x in input().split())

crafted = []

presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

while materials and magic_levels:
    material = materials.pop()
    magic_level = magic_levels.popleft()

    if material == 0 and magic_level == 0:
        continue
    if material == 0:
        magic_levels.appendleft(magic_level)
        continue
    if magic_level == 0:
        materials.append(material)
        continue

    product = material * magic_level

    if product in presents:
        crafted.append(presents[product])
    elif product < 0:
        materials.append(material + magic_level)
    else:
        materials.append(material + 15)

if ("Doll" in crafted and "Wooden train" in crafted) or \
   ("Teddy bear" in crafted and "Bicycle" in crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in reversed(materials))}")

if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

for toy in sorted(set(crafted)):
    print(f"{toy}: {crafted.count(toy)}")
from collections import deque

potions = {
    'Brew of Immortality': 110,
    'Essence of Resilience': 100,
    'Draught of Wisdom': 90,
    'Potion of Agility': 80,
    'Elixir of Strength': 70
}

substances = [int(x) for x in input().split(', ')]
crystals = deque(int(x) for x in input().split(', '))

crafted = set()
crafted_order = []

while len(crafted) < 5 and substances and crystals:
    substance = substances.pop()
    crystal = crystals.popleft()
    combined = substance + crystal

    if combined in potions.values():
        potion_name = next(k for k, v in potions.items() if v == combined)
        if potion_name not in crafted:
            crafted.add(potion_name)
            crafted_order.append(potion_name)
            continue

    candidates = [v for name, v in potions.items() if name not in crafted and v <= combined]

    if candidates:
        chosen_value = max(candidates)
        chosen_name = next(k for k, v in potions.items() if v == chosen_value)

        crafted.add(chosen_name)
        crafted_order.append(chosen_name)

        new_crystal = crystal - 20
        if new_crystal > 0:
            crystals.append(new_crystal)
    else:
        new_crystal = crystal - 5
        if new_crystal > 0:
            crystals.append(new_crystal)

if len(crafted) == 5:
    print("Success! The alchemist has forged all potions!")
else:
    print("The alchemist failed to complete his quest.")

if crafted_order:
    print("Crafted potions: " + ", ".join(crafted_order))

if substances:
    print("Substances: " + ", ".join(str(x) for x in reversed(substances)))

if crystals:
    print("Crystals: " + ", ".join(str(x) for x in crystals))
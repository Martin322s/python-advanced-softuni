def set_cover(universe, sets):
    universe = set(universe)
    chosen_sets = []

    while universe:
        best_set = max(sets, key=lambda s: len(universe & s))
        chosen_sets.append(best_set)
        universe -= best_set
        sets.remove(best_set)

    return chosen_sets


universe = list(map(int, input().split(', ')))
n = int(input())

sets = []
for _ in range(n):
    sets.append(set(map(int, input().split(', '))))

result = set_cover(universe, sets)

print(f"Sets to take ({len(result)}):")
for s in result:
    print(f"{{ {', '.join(map(str, sorted(s)))} }}")
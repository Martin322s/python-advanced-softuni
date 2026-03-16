from math import floor

def plant_garden(available_space, *allowed_plants, **requests):
    space_by_type = {plant_type: float(space) for plant_type, space in allowed_plants}
    planted = {}
    all_planted = True
    eps = 1e-9

    sorted_requests = sorted(requests.items(), key=lambda x: x[0])

    for i, (plant_type, qty) in enumerate(sorted_requests):
        qty = int(qty)

        if plant_type not in space_by_type:
            continue

        if available_space <= eps:
            for nxt_type, _ in sorted_requests[i:]:
                if nxt_type in space_by_type:
                    all_planted = False
                    break
            break

        space_per_piece = space_by_type[plant_type]
        can_plant = floor((available_space + eps) / space_per_piece)

        if can_plant <= 0:
            all_planted = False
            continue

        to_plant = min(qty, can_plant)
        planted[plant_type] = planted.get(plant_type, 0) + to_plant
        available_space -= to_plant * space_per_piece

        if to_plant < qty:
            all_planted = False

    if available_space < 0 and abs(available_space) < 1e-6:
        available_space = 0.0

    if all_planted:
        lines = [f"All plants were planted! Available garden space: {available_space:.1f} sq meters."]
    else:
        lines = ["Not enough space to plant all requested plants!"]

    lines.append("Planted plants:")
    for plant_type in sorted(planted):
        lines.append(f"{plant_type}: {planted[plant_type]}")

    return "\n".join(lines)
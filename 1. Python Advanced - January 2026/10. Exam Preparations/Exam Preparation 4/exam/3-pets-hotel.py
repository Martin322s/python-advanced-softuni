def accommodate_new_pets(available_capacity, pets_maximum_weight, *args):
    current_capacity = available_capacity
    pets_hotel = {}
    not_all_accommodated = False

    for pet_type, weight in args:
        if current_capacity == 0:
            not_all_accommodated = True
            break

        if weight > pets_maximum_weight:
            continue

        pets_hotel[pet_type] = pets_hotel.get(pet_type, 0) + 1
        current_capacity -= 1

    result = []
    if not not_all_accommodated:
        result.append(f"All pets are accommodated! Available capacity: {current_capacity}.")
    else:
        result.append("You did not manage to accommodate all pets!")

    result.append("Accommodated pets:")
    for pet_type in sorted(pets_hotel):
        result.append(f"{pet_type}: {pets_hotel[pet_type]}")

    return "\n".join(result)
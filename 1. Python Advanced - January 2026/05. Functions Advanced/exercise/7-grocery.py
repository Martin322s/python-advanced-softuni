def grocery_store(**kwargs):
    sorted_result = sorted(kwargs.items(), key=lambda kvp: (-kvp[1], -len(kvp[0]), kvp[0]))
    result = ""

    for product, quantity in sorted_result:
        result += f"{product}: {quantity}\n"

    return result
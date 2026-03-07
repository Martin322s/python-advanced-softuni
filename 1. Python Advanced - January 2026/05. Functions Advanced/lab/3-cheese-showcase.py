def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(), key=lambda item: (-len(item[1]), item[0]))
    result = ""

    for name, quantities in sorted_cheeses:
        result += f"{name}\n"
        for quantity in sorted(quantities, reverse=True):
            result += f"{quantity}\n"

    return result.strip()
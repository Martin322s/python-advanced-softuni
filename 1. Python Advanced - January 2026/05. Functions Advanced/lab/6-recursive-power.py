def recursive_power(base, exponent):
    if exponent < 0:
        raise ValueError("Exponent must be a non-negative integer.")
    if exponent == 0:
        return 1
    return base * recursive_power(base, exponent - 1)
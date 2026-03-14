def create_sequence(count):
    sequence = []

    a, b = 0, 1
    for _ in range(count):
        sequence.append(a)
        a, b = b, a + b

    return sequence


def locate_number(sequence, number):
    if number in sequence:
        return sequence.index(number)
    return -1
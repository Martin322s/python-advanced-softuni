def reverse_text(string):
    for el in range(len(string) - 1, -1, -1):
        yield string[el]
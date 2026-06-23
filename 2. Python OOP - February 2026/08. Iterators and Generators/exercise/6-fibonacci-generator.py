def fibonacci():
    a = 0
    b = 1
    result = 0

    while True:
        yield result
        a, b = b, a + b
        result = a
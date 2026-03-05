def math_operations(*args, **kwargs):
    operations = ["a", "s", "d", "m"]

    for i in range(len(args)):
        key = operations[i % 4]
        value = args[i]

        if key == "a":
            kwargs[key] += value
        elif key == "s":
            kwargs[key] -= value
        elif key == "d":
            if value != 0:
                kwargs[key] /= value
        elif key == "m":
            kwargs[key] *= value

    sorted_result = sorted(
        kwargs.items(),
        key=lambda x: (-x[1], x[0])
    )

    return "\n".join(f"{k}: {v:.1f}" for k, v in sorted_result)
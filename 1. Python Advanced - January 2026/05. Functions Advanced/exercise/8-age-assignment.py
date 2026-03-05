def age_assignment(*args, **kwargs):
    result = {}
    result_text = ""

    for name in args:
        first_letter = name[0]

        if first_letter in kwargs:
            result[name] = kwargs[first_letter]

    for name, age in sorted(result.items()):
        result_text += f"{name} is {age} years old.\n"

    return result_text
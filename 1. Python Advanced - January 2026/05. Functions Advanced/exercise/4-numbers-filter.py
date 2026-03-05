def even_odd_filter(**kwargs):
    if "odd" in kwargs:
        kwargs["odd"] = [num for num in kwargs["odd"] if num % 2 != 0]

    if "even" in kwargs:
        kwargs["even"] = [num for num in kwargs["even"] if num % 2 == 0]

    return dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))
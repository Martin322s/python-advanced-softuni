def type_check(type_to_check):
    def decorator(func):
        def wrapper(num):
            if type(num) == type_to_check:
                return func(num)
            else:
                return "Bad Type"
        return wrapper
    return decorator
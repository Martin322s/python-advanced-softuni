def even_parameters(func):
    def wrapper(*args):
        list = [el for el in args if isinstance(el, int) and el % 2 == 0]
        all_even = len(list) == len(args)
        if all_even:
            return func(*list)
        else:
            return "Please use only even numbers!"
    return wrapper

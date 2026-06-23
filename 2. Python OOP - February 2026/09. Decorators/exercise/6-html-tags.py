def tags(tag):
    def decor(func):
        def wrapper(*args):
            string = func(*args)
            return f"<{tag}>{string}</{tag}>"
        return wrapper
    return decor
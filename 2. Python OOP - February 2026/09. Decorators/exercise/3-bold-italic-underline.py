def make_bold(func):
    def wrapper(*args):
        open = '<b>'
        close = '</b>'
        return open + func(*args) + close
    return wrapper

def make_italic(func):
    def wrapper(*args):
        open = '<i>'
        close = '</i>'
        return open + func(*args) + close
    return wrapper

def make_underline(func):
    def wrapper(*args):
        open = '<u>'
        close = '</u>'
        return open + func(*args) + close
    return wrapper
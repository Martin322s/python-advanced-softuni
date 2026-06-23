def cache(func):
    log = {}

    def wrapper(n):
        if n in log:
            return log[n]

        result = func(n)
        log[n] = result
        return result

    wrapper.log = log
    return wrapper
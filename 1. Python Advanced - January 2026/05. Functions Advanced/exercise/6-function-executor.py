def func_executor(*args):
    result = ""
    for execution in args:
        func, func_args = execution
        func_result = func(*func_args)
        result += f"{func.__name__} - {func_result}\n"

    return result
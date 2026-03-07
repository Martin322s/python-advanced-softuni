def operate(symbol, *args):
    if symbol == '+':
        return sum(args)
    elif symbol == '-':
        if len(args) == 0:
            raise ValueError("At least one operand is required for subtraction.")
        result = args[0]
        for num in args[1:]:
            result -= num
        return result
    elif symbol == '*':
        result = 1
        for num in args:
            result *= num
        return result
    elif symbol == '/':
        if len(args) == 0:
            raise ValueError("At least one operand is required for division.")
        result = args[0]
        for num in args[1:]:
            if num == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            result /= num
        return result
    else:
        raise ValueError(f"Unsupported operation: {symbol}")
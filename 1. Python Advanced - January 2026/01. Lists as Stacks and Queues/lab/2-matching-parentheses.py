def extract_parentheses(expression):
    stack = []
    result = []

    for i, ch in enumerate(expression):
        if ch == '(':
            stack.append(i)
        elif ch == ')':
            start = stack.pop()
            result.append(expression[start:i+1])

    return result


expr = input()
parentheses = extract_parentheses(expr)

for p in parentheses:
    print(p)
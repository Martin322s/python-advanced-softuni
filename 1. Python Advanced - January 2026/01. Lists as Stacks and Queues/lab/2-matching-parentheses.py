expression = input()

stack = []

for i, ch in enumerate(expression):
    if ch == '(':
        stack.append(i)
    elif ch == ')':
        start_idx = stack.pop()
        print(expression[start_idx:i + 1])
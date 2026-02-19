parentheses = input()

stack = []
balanced = True

for char in parentheses:
    if char in "({[":
        stack.append(char)
    else:
        if not stack:
            balanced = False
            break

        top = stack[-1]
        if (top == "(" and char == ")") or (top == "{" and char == "}") or (top == "[" and char == "]"):
            stack.pop()
        else:
            balanced = False
            break

if balanced and not stack:
    print("YES")
else:
    print("NO")
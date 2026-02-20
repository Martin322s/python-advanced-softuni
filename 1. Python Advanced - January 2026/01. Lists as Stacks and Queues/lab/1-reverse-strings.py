text = input()

stack = list(text)
reversed_text = []

while stack:
    reversed_text.append(stack.pop())

print(''.join(reversed_text))
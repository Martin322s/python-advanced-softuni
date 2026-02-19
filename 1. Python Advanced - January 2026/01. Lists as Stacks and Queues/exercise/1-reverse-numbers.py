numbers_input = [int(x) for x in input().split(" ") if x]

numbers_stack = []

for i in range(len(numbers_input)):
    numbers_stack.append(numbers_input[i])

while len(numbers_stack):
    print(numbers_stack.pop(), end=" ")
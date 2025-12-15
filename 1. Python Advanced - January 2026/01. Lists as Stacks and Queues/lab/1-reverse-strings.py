text = input()

string_stack = []
result = ""

for i in range(len(text)):
    string_stack.append(text[i])

while len(string_stack):
    result += string_stack.pop()

print(result)
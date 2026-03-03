input_line = input()

parts = input_line.split("|")
result = []

for i in range(len(parts) - 1, -1, -1):
    numbers = parts[i].split()
    for num in numbers:
        result.append(num)

print(" ".join(result))
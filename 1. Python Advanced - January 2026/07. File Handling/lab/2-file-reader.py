file = open("numbers.txt")
sum = 0

for num in file:
    sum += int(num)

print(sum)
file.close()
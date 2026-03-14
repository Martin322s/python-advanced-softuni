from math_operations import calculate

expression = input().split()

num1 = float(expression[0])
sign = expression[1]
num2 = int(expression[2])

result = calculate(num1, sign, num2)

print(f"{result:.2f}")
students_count = int(input())

data = {}

for _ in range(students_count):
    name, grade = input().split()
    grade = float(grade)
    if name not in data:
        data[name] = []
    data[name].append(grade)

for name, grades in data.items():
    average_grade = sum(grades) / len(grades)
    grades_formatted = ' '.join(f"{grade:.2f}" for grade in grades)
    print(f"{name} -> {grades_formatted} (avg: {average_grade:.2f})")
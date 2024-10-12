class_grades = {
    "Alice": [90, 85, 95],
    "Bob": [80, 75, 85],
    "Charlie": [95, 90, 92],
    "David": [88, 82, 90],
  "rohit verma" : [50,86,90]
}

for student, grades in class_grades.items():
    total = 0
    for grade in grades:
        total += grade
    average = total / len(grades)
    print(f"{student}'s average grade is: {average:.2f}")

total_grades = []
for grades in class_grades.values():
    total_grades.extend(grades)
overall_average = sum(total_grades) / len(total_grades)
print(f"Overall class average: {overall_average:.2f}")

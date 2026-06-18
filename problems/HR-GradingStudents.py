# HackerRank - Grading Students
n = int(input())
grades = []
for _ in range(n):
    grades.append(int(input()))
for grade in grades:
    if grade < 38:
        print(grade)
    else:
        next_multiple = ((grade // 5) + 1) * 5
        if next_multiple - grade < 3:
            print(next_multiple)
        else:
            print(grade)
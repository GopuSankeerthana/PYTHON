n = int(input())
students = []

for i in range(n):
    name = input()
    score = float(input())
    students.append([name, score])

scores = sorted(set(score for name, score in students))
second = scores[1]

for name in sorted(name for name, score in students if score == second):
    print(name)
marks = [29,19,30,23,27]
print("max mark:",max(marks))
for i in marks:
    if i == max(marks):
        print("max mark:",i)

#without using max function
max_mark = max(marks)
for i in marks:
    if i > max_mark:
        print("max mark:",i)
        
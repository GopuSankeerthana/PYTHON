maths = int(input("Enter your Maths marks: "))
science = int(input("Enter your Science marks: "))
english = int(input("Enter your English marks: "))

total_marks = maths + science + english
average_marks = total_marks / 3

if average_marks >= 90:
    grade = "A"
elif average_marks >= 80:
    grade = "B"
elif average_marks >= 70:
    grade = "C"
elif average_marks >= 60:
    grade = "D"
else:
    grade = "F"

print(f"\nTotal Marks   : {total_marks}"
      f"\nAverage Marks : {average_marks:.2f}"
      f"\nGrade         : {grade}")
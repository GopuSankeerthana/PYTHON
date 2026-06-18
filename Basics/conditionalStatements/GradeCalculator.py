#program to calculate the grade of a student based on their marks
marks = float(input("Enter the marks obtained: "))
if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
elif marks >= 40:
    print("Grade: F")
else:
    print("Fail")
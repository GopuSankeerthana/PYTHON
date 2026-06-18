marks = float(input("Enter your marks: "))
attendance = float(input("Enter your attendance percentage: "))
if marks >= 95:
    print("You are eligible for a scholarship of $2000.")
elif marks >= 85 and attendance >= 90:
    print("You are eligible for a scholarship of $1000.")
else:
    print("You are not eligible for any scholarship.")
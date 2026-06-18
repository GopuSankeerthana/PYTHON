#program to whether the person is eligible to vote or not
age = int(input("Enter your age: "))
if age>0:
    if age >= 18:
        print("You are eligible to vote.")
    else: 
        print("You are not eligible to vote.")
else:
    print("Please enter a valid age.")
#program to check whether a person is eligible to withdraw money from ATM or not
balance = float(input("Enter your account balance: "))
if balance>=0:
    if balance >= 1000:
        print("You are eligible to withdraw money from ATM.")
    else:
        print("You are not eligible to withdraw money from ATM. Minimum balance required is 1000.")
else:
    print("Please enter a valid account balance.")
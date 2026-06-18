#program to find the amount of shopping discount based on the total bill amount and membership status
total_bill = float(input("Enter the total bill amount: "))
membership_status = input("Are you a member? (yes/no): ").lower()
if membership_status == "yes" and total_bill >= 5000:
    print(f"You are eligible for a discount of 25%. Your discounted bill amount is: {total_bill * 0.75}")
elif membership_status == "yes" and total_bill >= 2000:
    print(f"You are eligible for a discount of 15%. Your discounted bill amount is: {total_bill * 0.85}")
elif membership_status == "no" and total_bill >= 5000:
    print(f"You are eligible for a discount of 10%. Your discounted bill amount is: {total_bill * 0.90}")
else:
    print("sorry! You are not eligible for any discount. Your bill amount is: ", total_bill)
    
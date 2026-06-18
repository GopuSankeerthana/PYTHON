#program to find the amount of income tax to be paid based on the slabs of income tax
income = float(input("Enter your annual income: "))
if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = (income - 250000) * 0.05
elif income <= 1000000:
    tax = (income - 500000) * 0.2 + 12500
else:
    tax = (income - 1000000) * 0.3 + 112500
print(f"The amount of income tax to be paid is: {tax}")

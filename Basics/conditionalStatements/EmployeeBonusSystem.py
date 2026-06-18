#program to fine the employee bonus system based on the years of service and performance rating
employee_name = input("Enter the employee's name: ")
years_of_service = int(input("Enter the years of service: "))
performance_rating = input("Enter the performance rating(EXCELLENT or GOOD or AVERAGE): ").upper()
if years_of_service >= 5 and performance_rating == "EXCELLENT":
    print(f"{employee_name} is eligible for a bonus of 20% of the annual salary.")
elif performance_rating == "GOOD":
        print(f"{employee_name} is eligible for a bonus of 10% of the annual salary.")
elif performance_rating == "AVERAGE":
        print(f"{employee_name} is eligible for a bonus of 5% of the annual salary.")
else:
    print(f"{employee_name} is not eligible for any bonus.")
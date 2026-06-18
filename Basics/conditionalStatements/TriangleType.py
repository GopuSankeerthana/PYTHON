#program to find the type of triangle based on the lengths of its sides
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))
if side1 <= 0 or side2 <= 0 or side3 <= 0:
    print("Please enter valid lengths for the sides of the triangle.")
elif side1 == side2 == side3:
    print("The triangle is equilateral.")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")

    
    
    
    
    
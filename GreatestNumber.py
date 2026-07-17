n1, n2, n3 = map(int, input("Enter three numbers separated by space: ").split())

if n1 >= n2 and n1 >= n3:
    greatest = n1
elif n2 >= n1 and n2 >= n3:
    greatest = n2
else:
    greatest = n3

print(f"The greatest number among {n1}, {n2}, and {n3} is: {greatest}")
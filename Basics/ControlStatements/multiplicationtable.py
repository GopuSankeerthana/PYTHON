n = int(input("Enter a number: "))
m = int(input("enter a num such that how many multiples do you want: "))
for i in range(1, m+1):
    print(f"{n} x {i} = {n*i}")
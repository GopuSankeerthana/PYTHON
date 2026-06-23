n = int(input("Enter a number: "))
temp = n
rev = 0
while temp > 0:
    rev = temp % 10 + rev * 10
    temp = temp // 10
if n == rev:
    print(n, "is a palindrome number")
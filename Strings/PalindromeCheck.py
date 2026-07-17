s1 = input("Enter a string to check if it is a palindrome: ")
reverse = s1[::-1]
if s1 == reverse:
    print(f"{s1} is a palindrome.")
else:
    print(f"{s1} is not a palindrome.")
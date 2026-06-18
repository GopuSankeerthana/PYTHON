password = input("Enter your password: ")
isDigit = False
isUpper = False
isLower = False
isSpecial = False
for char in password:
    if char.isdigit():
        isDigit = True
    elif char.isupper():
        isUpper = True
    elif char.islower():
        isLower = True
    elif not char.isalnum():
        isSpecial = True
length = len(password)
if length >= 8 and isDigit and isUpper and isLower and isSpecial:
    print("Strong password")
elif length >= 6 and (isDigit and isUpper and isLower):
    print("Moderate password")
else:
    print("Weak password")
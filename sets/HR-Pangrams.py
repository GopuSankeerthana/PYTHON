s = input().lower()

letters = set()

for ch in s:
    if ch.isalpha():
        letters.add(ch)

if len(letters) == 26:
    print("pangram")
else:
    print("not pangram")
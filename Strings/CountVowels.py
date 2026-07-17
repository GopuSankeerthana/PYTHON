s = "Hello, how many vowels are in this string?"
print(s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u'))
#method 2
def count_vowels(s):
    s.lower()
    vowels = 'aeiou'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
print(count_vowels(s))   
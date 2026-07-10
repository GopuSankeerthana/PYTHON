def twoStrings(s1, s2):
    return "YES" if set(s1) & set(s2) else "NO"

t = int(input())
for _ in range(t):
    s1 = input().strip()
    s2 = input().strip()
    print(twoStrings(s1, s2))
s = [1,3,2,4,5]
target = 6
for i in range(len(s)):
    for j in range(i+1, len(s)):
        if s[i] + s[j] == target:
            print(f"Pair found: ({s[i]}, {s[j]})")
            break
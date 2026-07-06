a = [100 , 4, 200, 1,5 ,2]
s = set(a)
longest = 0
for i in s:
    if i-1 not in s:
        count = 1
        while i+count in s:
            count += 1
        longest = max(longest, count)
print(longest)
        
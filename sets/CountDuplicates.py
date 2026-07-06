a = [1,4,3,2,1,3,4,5,2,1]
freq = {}
for num in a:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
for i in freq:
    if freq[i] > 1:
        print(i)

# method 2 using set
s1 = set(a)
print(s1)